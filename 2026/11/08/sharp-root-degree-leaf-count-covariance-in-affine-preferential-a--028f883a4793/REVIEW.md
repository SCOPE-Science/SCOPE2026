# Independent mathematical audit

## correctness

PASS

Let a=1+δ>0, b=2+δ, S_n=bn-2, R_n=E(D_n+δ), h_n=P(D_n=1), M_n=E L_n. The exact conditional attachment and leaf-update indicators yield R_{n+1}=(1+1/S_n)R_n, h_{n+1}=(1-a/S_n)h_n, M_{n+1}=(1-a/S_n)M_n+1 and C_{n+1}=(1-δ/S_n)C_n+aR_nM_n/S_n²-ah_n/S_n. Identities R_n=(S_n-a)h_n and M_n=(S_n+2b h_n)/(3+2δ) make forcing positive n>=3, proving C_n>0 n>=4 and C_4=a(2+δ)/(2(4+3δ)²). A gamma product gives R_n~a Γ(2-2/b)/Γ(2-1/b)n^(1/b); subtract R_n/(3+2δ) and bound the inhomogeneous remainder O(n^(2/b-1))=o(R_n). Thus C_n/R_n→1/(3+2δ) for every fixed real δ>-1. Independent exact rational exhaustive attachment-history enumeration verifies n<=8 at δ=-1/2,0,1.

## originality

PASS

The exact δ=0 Barabási–Albert oldest-hub covariance and its 2 sqrt(n)/(3 sqrt(pi)) constant were already proved Oct13 and are not credited new. The November 2 birth-age theorem also concerns δ=0 and later-born vertices. A distinct November 2 plane-oriented recursive-tree study has attachment proportional to 1+α number-of-children from a single root, not the same δ-affine undirected-degree attachment from an initial edge, so its old-child covariance formulas do not supply the present all-real-δ root-degree/leaf law. The surviving theorem gives strict positivity and exact coefficient/exponent continuously for δ>-1. Originality qualified against unlocated broader affine urn formulas.

## value

PASS

A quantified covariance of a persistent initial hub degree with the global fringe in affine preferential attachment is a natural local-global dependence observable. Its strictly positive sign for every n>=4 and universal offset-dependent ratio 1/(3+2δ), including the power n^{1/(2+δ)}, show a nontrivial continuous family rather than the already-known δ=0 example. Such exact mixed-moment scaling can serve as a benchmark for joint fluctuations in nonstationary attachment processes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
