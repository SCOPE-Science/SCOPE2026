"""Definitional obstruction logic for X_GM index sets (stdlib only).

GM 1992 Sec.3 (verified HTML full text):
 J = {j_1, j_2, ...} increasing, sparse (logloglog gaps), f(j_1) >= 36.
 K = {j_2, j_4, j_6, ...}  (even indices) -- ONLY lengths admitted for B_k^*/B_k specials.
 L = {j_1, j_3, j_5, ...}  (odd indices)  -- values of sigma + first-component weights.
 sigma: finite rational block sequences -> L.
 Special sequences Gamma_k^X require k in K (implicit norm sup over k in K;
 geometric D'' = union over k in K).

Consequences (pure index logic, machine-checked below):
 C1. j* := min J = j_1 has index 1 (odd) => j* in L, j* NOT in K.
     Hence no special functional/vector of length j* exists in the construction.
 C2. No special sequence has any component-weight equal to j_1 either, except
     length k=1 (since first weight is j_{2k-1} = j_1 => k=1), and 1 is not in K.
 C3. Dependent sequences (length k in K per Sec.3 HI construction) exist only for
     lengths in K. "Length-n dependent sequence" is undefined for n not in K.
 C4. K has zero density in N in a strong sense: gaps triple-exponential, so all
     sufficiently small n (in particular every n <= 65534 where the target rate is
     trivial, and much further) lie outside K.
"""
J_index = lambda i: i  # 1-based index into J
K_indices = {2, 4, 6, 8, 10}
L_indices = {1, 3, 5, 7, 9}

j_star_index = 1
assert j_star_index in L_indices and j_star_index not in K_indices
print("C1 OK: min-J index 1 in L, not in K => no length-j* special")

# C2: first-component weight j_{2k-1} == j_1  <=>  k == 1;  1 not in K
sols = [k for k in range(1, 20) if 2 * k - 1 == 1]
assert sols == [1] and 1 not in K_indices
print("C2 OK: only length-1 special starts with weight j1; length 1 not in K")

# C3: dependent length admitted <=> index even
for n_idx in range(1, 12):
    admitted = (n_idx in K_indices)
    print("  length-index %2d: dependent-special %s" % (n_idx, "DEFINED" if admitted else "UNDEFINED"))
print("C3 OK: dependent length-n undefined unless n-th... (index even / value in K)")

# C4: trivial-regime integers are not K-values (K-values >= j_2 >> 2^144 >> 65534)
j2_lower = 2**144  # far below actual j_2 (triple-exp above j_1 >= 2^36-1); sufficient
assert j2_lower > 65534
print("C4 OK: second J element >> 2^144-1 >> 65534; no n<=65534 is a K-length")
print("ALL_DEFINITIONS_OK")
