import numpy as np
B = np.array([[2,1],[1,1]], dtype=float)
lam = (3+np.sqrt(5))/2  # ~2.618
mu = 1/lam
print("lam", lam, "mu", mu)
# eigenvectors (symmetric B so orthogonal)
# e_u for lam, e_s for mu
w, V = np.linalg.eigh(B)
print("eigvals", w)
print("eigvecs", V)
# e_s ~ eigenvalue mu, e_u ~ lam
