# Independent mathematical audit

## correctness

PASS

Two translated orthonormal Fock jet clusters give Gram block [I C;C* I] with C=P_mD_rP_m, hence spectrum 1±σ_j(C); leakage A=(I−P_m)D_rP_m satisfies A*A=I−C*C. The m distinct leakage singular-value orders are extracted from the unique leading p×p exterior minor: rows m..m+p−1, columns m−p..m−1, of order r^{p²}, coefficient c_{m,p}=sqrt(prod_i (m+i)!/(m−p+i)!)*prod_i i!/(p+i)!. All other minors vanish at higher order and analytic Fock tails are controlled. Ratios of exterior norms give s_{m,p}~(c_{m,p}/c_{m,p−1})r^{2p−1}=γ_{m,p}r^{2p−1}; squaring/2 yields λ^-~γ²r^{4p−2}/2, sharp smallest λ and condition number. At m=2 direct singular values give exact λ_min=1−exp(−r²/2)(sqrt(4+r^4)+r²)/2. Independent mpmath displaced-monomial computations for m=1..4 at r=.035 checked all leading constants within ~0.13% and exact block identity. Only fixed-m local r→0 is proven.

## originality

PASS

PASS best-of-knowledge: classical Weyl-displaced Fock matrix elements and RKHS representer/interpolation results are known; multiple-Fock interpolation density/geometric criteria are also prior. These do not as inspected yield the explicit m-level two-cluster jet Gram spectrum and sharp factorial constants. The older 1991 displaced-Fock full text and other coherent-state conditioning literature were not accessible and remain named risks; absence of a match is not proof of worldwide novelty.

## value

PASS

PASS: Colliding Hermite/Fock evaluation clusters form a natural conditioning problem in RKHS interpolation. A complete distinct hierarchy r^{4p−2}, with explicit constants and worst singular-value exponent 4m−2 for every m, quantifies precisely which jet directions become unidentifiable; this is meaningful structural spectral information beyond merely asserting instability or finite experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
