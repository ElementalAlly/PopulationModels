def list_to_vector(l):
    result = []
    for i in l:
        result.append([i])
    return result


def m_product(m1, m2):
    if len(m1[0]) != len(m2):
        return None
    common_dimension = len(m2)
    r = []
    for i1 in range(len(m1)):
        append_list = []
        for j2 in range(len(m2[0])):
            r_sum = 0
            for common in range(common_dimension):
                r_sum += m1[i1][common] * m2[common][j2]
            append_list.append(r_sum)
        r.append(append_list)
    return r


def m_print(m):
    for r in m:
        r_str = f"[{r[0]}"
        for i in range(len(r) - 1):
            r_str += f"  {r[i+1]}"
        r_str += "]"
        print(r_str)
    print()
    return


def reduce_matrix(m, d, r, c):
    red_ind_r = [j for j in range(d) if j != r]
    red_ind_c = [j for j in range(d) if j != c]
    red_matrix = []
    for s in red_ind_r:
        append_list = []
        for t in red_ind_c:
            append_list.append(m[s][t])
        red_matrix.append(append_list)
    return red_matrix


def det(m, d):
    if d <= 0:
        return None
    if d == 1:
        return m[0][0]
    r = 0
    for i in range(d):
        red_matrix = reduce_matrix(m, d, 0, i)
        c = 1 if i % 2 == 0 else -1
        r += c * m[0][i] * det(red_matrix, d-1)
    return r


def inverse(m, d):
    total_det = det(m, d)
    result = []
    for r in range(d):
        append_list = []
        for c in range(d):
            coeff = 1 if (r + c) % 2 == 0 else -1
            append_list.append(coeff * det(reduce_matrix(m, d, c, r), d-1) / total_det)
        result.append(append_list)
    return result


def v_print(v):
    r = f"[{v[0][0]}"
    for i in range(1, len(v)):
        r += f", {v[i][0]}"
    r += "]"
    print(r)
    return


init_pop_list = [289, 211, 120, 76, 51]

basic_trans = [[0, 1, 1.9, 1.7, 0],
               [0.61, 0, 0, 0, 0],
               [0, 0.33, 0, 0, 0],
               [0, 0, 0.21, 0, 0],
               [0, 0, 0, 0.13, 0.08]]

"""
basic_inv = [[0, 1.639, 0, 0, 0],
             [0, 0, 3.03, 0, 0],
             [0, 0, 0, 4.762, 0],
             [0.588, 0, -1.782, -5.32, 0.004],
             [-0.956, 0, 2.897, 8.65, 12.501]]
"""

basic_inv = inverse(basic_trans, 5)

proposed_fishing_trans = [[0, 1, 1.8, 1.7, 0],
                          [0.61, 0, 0, 0, 0],
                          [0, 0.29, 0, 0, 0],
                          [0, 0, 0.19, 0, 0],
                          [0, 0, 0, 0.13, 0.08]]

past_pop_vector = list_to_vector(init_pop_list)
print("Into past")
for i in range(25):
    print(f"{2 * i + 2} years ago:")
    past_pop_vector = m_product(basic_inv, past_pop_vector)
    v_print(past_pop_vector)


natural_pop_vector = list_to_vector(init_pop_list)
print("Into future (natural)")
for i in range(25):
    print(f"{2 * i + 2} years ahead:")
    natural_pop_vector = m_product(basic_trans, natural_pop_vector)
    v_print(natural_pop_vector)


proposed_fishing_pop_vector = list_to_vector(init_pop_list)
print("Into future (proposed fishing)")
for i in range(25):
    print(f"{2 * i + 2} years ahead:")
    proposed_fishing_pop_vector = m_product(proposed_fishing_trans, proposed_fishing_pop_vector)
    v_print(proposed_fishing_pop_vector)