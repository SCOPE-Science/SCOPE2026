import sympy as sp

k = sp.symbols("k", real=True)

# Adapted horizontal basis: phi and G are skew orthogonal complex structures
# satisfying G*phi = -phi*G.
J = sp.Matrix([
    [0,-1,0,0],
    [1,0,0,0],
    [0,0,0,-1],
    [0,0,1,0],
])
G = sp.Matrix([
    [0,0,-1,0],
    [0,0,0,1],
    [1,0,0,0],
    [0,-1,0,0],
])
I = sp.eye(4)

assert J.T == -J
assert G.T == -G
assert J*J == -I
assert G*G == -I
assert J*G + G*J == sp.zeros(4)

K = 2*(k*J-G)
assert K.T == -K
assert sp.simplify(K*K + 4*(k**2+1)*I) == sp.zeros(4)
assert sp.simplify(K.T*K - 4*(k**2+1)*I) == sp.zeros(4)

# Matrix of the two-form omega(e_i,e_j)=<K e_i,e_j>.
W = K.T
pf = sp.expand(W[0,1]*W[2,3] - W[0,2]*W[1,3] + W[0,3]*W[1,2])
assert sp.simplify(pf - 4*(k**2+1)) == 0
wedge_coeff = sp.expand(2*pf)
assert sp.simplify(wedge_coeff - 8*(k**2+1)) == 0

# Published norm check: a four-dimensional skew operator with two equal
# singular values 2*sqrt(k^2+1) has two-form norm squared 8*(k^2+1).
twoform_norm_sq = sp.simplify(sp.trace(K.T*K)/2)
assert twoform_norm_sq == 8*(k**2+1)

print("VERIFY_OK")
print("horizontal_square=-4*(k^2+1)*I")
print("equal_skew_singular_values=2*sqrt(k^2+1)")
print("contact_volume_norm=8*(k^2+1)")
print("published_norm_match=true")
