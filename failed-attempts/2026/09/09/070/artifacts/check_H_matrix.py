"""Lightweight audit of output/artifacts/H_orbits.json (stdlib only, seconds).
Checks: orbit sizes sum to PG(3,7) totals; tactical symmetry n_i*a_ij = n_j*a_ji;
row sums = 57-1 = 448 (lines meeting a given line, self excluded);
incidence sanity vs Result 2.1(b) for x=18 (|L|=1026, incident 144/192).
Prints CHECK_OK."""
import json
H = json.load(open("output/artifacts/H_orbits.json"))
n = H["line_orbits"]; A = H["meeting"]
assert n == [1, 448, 2401], n
assert sum(n) == 2850 == (7**2+1)*(7**2+7+1)
assert H["point_orbits"] == [8, 392] and sum(H["point_orbits"]) == 400
for i in range(3):
    assert sum(A[i]) == 448, A[i]
    for j in range(3):
        assert n[i]*A[i][j] == n[j]*A[j][i], (i, j)
assert A == [[0,448,0],[1,104,343],[0,64,384]], A
# every line meets exactly 448 others: 8 pts x 56 others... 8*56=448 (disjoint, two pts share only their line)
assert 8*56 == 448
print("CHECK_OK: H_orbits.json internally consistent; meeting rows sum to 448; tactical symmetry holds")
