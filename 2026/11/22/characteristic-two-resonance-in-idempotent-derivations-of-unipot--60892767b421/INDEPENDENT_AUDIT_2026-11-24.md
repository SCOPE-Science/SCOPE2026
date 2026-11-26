# Independent mathematical audit

## correctness

PASS

The derived ideal is R because T is invertible. The resulting condition is [B,T]=aT and composition idempotence adds a=0 or 1, B²=B, Bu=(1−a)u. In the zero branch the cyclic commutant is the local ring k[x]/(x^N). In the one branch, T shifts the projection eigenvalues by one; outside characteristic two it annihilates the one-eigenspace, an impossibility, and in characteristic two it exchanges the two eigenspaces, giving N=2m. The Euler derivation in y=1+x descends in exactly the required even characteristic-two case and is idempotent; other commutator solutions differ by multiplication. Squaring gives the stated quadratic equation. With z=x² and c=A+yC, this is A²+A+(1+z)C²=0; the constant coefficient is eliminated by a₀=(a₀+b₀)², and every higher a_j is determined by earlier indices. This gives polynomial inverse coordinates and does not need a perfect field. Rank m+1 and the bracket equality follow from T(E₁)=E₀ and im D=k(t+u)⊕E₁. Over F_q there are q^m choices each of c and u; at N=2 the contributions occupy the same rank. An independent bounded replay (python3 /workspace/independent_sanity.py) exhausted raw matrices at (q,N)=(2,2),(3,2),(2,3), giving respectively {0:1,2:8}, {0:1,2:9}, {0:1,3:8}, and checked the exceptional brackets against the kernel at (2,2). The frozen verification note overstates the supplied checker: it tests the derivation equation and rank but does not separately assert the image-bracket identity. The independent proof establishes that identity for the entire stated range.

## originality

PASS

Verified prior work supplies the general linear derivation reduction, not the single-unipotent-block composition-idempotent classification, exceptional affine locus and labeled rank census. Closely indexed results change the algebra or operator identity. The scoped distinction is supported on the inspected evidence, without a global priority claim.

## value

PASS

A single invertible Jordan block is the natural indecomposable unipotent action. The all-dimension rank census identifies an extra family of the same population as the ordinary nonzero branch under a sharp characteristic/parity switch, and explains how a projection derivation can have brackets spanning its entire kernel. These structural and labeled-count conclusions go beyond the general block equation or a small-dimensional example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
