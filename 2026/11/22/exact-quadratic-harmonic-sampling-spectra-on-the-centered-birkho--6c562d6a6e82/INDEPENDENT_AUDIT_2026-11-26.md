# Independent mathematical audit

## correctness

PASS

The theorem is unchanged. The frozen SLOGAN's 'every Birkhoff polytope' omitted n≥4, and 'just three ... levels' did not distinguish sectors from eigenvalues at n=4. The universal scope without truncation is false (at n=2 the proposed nullity is −2). The complete replacement SLOGAN now states n≥4, three sectors with a collision at n=4, and the ratio for squared singular values. For the theorem, V_n is End(Std) in orthonormal bases and has dimension m=(n−1)². Centered permutation inner products are (f−1)/(n−1). The spherical fourth moment gives ⟨x^TAx,x^TBx⟩=2 tr(A*B)/(m(m+2)) for trace-free symmetric A,B; applying the resulting reproducing kernel to rank-one tensors gives K(x,y)=h2(mt²−1)/(m−1), t=⟨x,y⟩. Thus EE* is (h2/n!) times the stated fixed-point Gram f(f−2)/(n(n−2)). Subtract the point module from the two-subset permutation module to get χ2, and use the exterior square of Std to get χ3. Together with χ1=f−1 their sum is f(f−2), valid at n=4 as well. The normalized character operators on the regular representation are orthogonal central projections scaled by 1/d_j with dimensions d_j²; this identifies exactly the positive squared spectrum of E*E. Subtracting from h2 gives the cubic nullity, with d1=d3=3 at n=4 and d1<d2<d3 for n≥5, giving the asserted ratios and asymptotic visible fraction. The orbit has zero mean and scalar covariance by the irreducible left/right action. Polynomial exactness through degree four would give exact norms for every degree-two harmonic, contradicting the nonzero kernel. Independent exact check: python /workspace/branches/independent_math_1_4.py 4 constructs the Gram from integer-centered permutation matrices, verifies an annihilating polynomial and trace moments on its candidate eigenvalues at n=4,5, with harmonic nullities 22 and 58. The frozen scripts were inspected, not run. This finite check does not replace the character proof.

## originality

PASS

Classical Specht decomposition, spherical kernels and finite-group Fourier projections are credited. The distinct assessed result is the complete evaluated trace-free quadratic sampling operator of the centered Birkhoff orbit, including the normalized eigenvalues, multiplicities, harmonic nullity and sharp positive conditioning. The slogan repair does not expand that claim. No inspected theorem on comparable orbit sampling directly contains this instance.

## value

PASS

Normalized Birkhoff vertices give a canonical isotropic orbit. The exact all-n positive condition ratio and cubic invisible space resolve the first nonlinear sampling question, which cannot be read off second-moment tightness or dimension alone. The orbit-to-character computation yields a complete normalized spectral answer usable in inversion on the visible space rather than only a known-design observation or isolated small-n check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
