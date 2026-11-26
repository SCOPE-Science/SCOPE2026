# Independent mathematical audit

## correctness

PASS

With probability surface measure the kernel on S3 is (l+1)U_l, using dimension (l+1)^2. For all 24 nodes the parity block doubles the representative spectrum and adds 12 zeros. For even l the root-line adjacency A is the line graph of K4 on supports, tensored with the two-by-two all-ones matrix. The incidence product gives A-eigenvalues 8, -4, 0 with sector dimensions 1, 2, 9. The Gram matrix B_l=(l+1-beta)I+(alpha-beta)A+beta J then has the asserted three sectors. In the odd case the signed matrix S=M* M-2I for columns e_i±e_j has eigenvalues 4 and -2 with dimensions 4 and 8, since M M*=6I, and B_l=(l+1)I+alpha S. Substituting the six-periodic alpha and alternating even beta gives ranks (1,4,9,8,11,12,10,12,12,12,11) up to degree 10. For even l>=12 the three eigenvalues have lower bounds l-10,l-6,l, and for odd l>=5 the two have bounds l-3,l-1, giving the sharp cutoff 11. In full-rank odd degrees tightness is exactly alpha=0, i.e. l=5 mod 6. In even degrees equal values would require first alpha=0 and then beta=0, impossible. The representative kernel Gram is (l+1)^2 I at tight degrees, so the minimum squared norm is the representative data norm squared divided by (l+1)^2; the parity-compatible full data norm squared is twice the representative value.

## originality

FAIL

The complete claimed spectrum is a direct finite Fourier consequence of pre-existing binary-tetrahedral character and all-degree SU(2) branching data, not merely a match to the mean-zero design theorem or a postdated catalogue hit. Rotate the D4 nodes by (a,b,c,d) -> (a+b,a-b,c+d,c-d)/sqrt(2); this gives the eight signed coordinate units and sixteen half-coordinate sign vectors, the Hurwitz unit group 2T. For g,h in 2T the unscaled full Gram entry is U_l(Re(g^(-1)h))=chi_{Sym^l}(g^(-1)h). Thus ordinary Schur orthogonality on the regular representation gives the full-block eigenvalue 24 m_rho(l)/dim(rho), of multiplicity dim(rho)^2, where m_rho(l) is the symmetric-power branching multiplicity. Suter's pre-existing character table and class sizes give these by a single character inner product. Set L=l+1. At even l, for irreps 1,1',1'',3 respectively they are (L+3beta+8alpha)/12, (L+3beta-4alpha)/12, (L+3beta-4alpha)/12, (L-beta)/4. At odd l, for 2,2',2'' respectively they are (L+4alpha)/6, (L-2alpha)/6, (L-2alpha)/6. All opposite central-parity multiplicities vanish. For example, the even trivial coefficient has contributions 2L from the two central elements, 6beta from trace zero and 16alpha from the four size-four classes of traces ±1; the twisted character replaces 16alpha by -8alpha since the two nontrivial cube roots sum to -1. Dividing the unscaled full nonzero-parity block by two for representatives gives exactly every frozen eigenvalue and multiplicity. Sharp rank, tight degrees and the normalized interpolant norm then follow by the same scalar substitutions and the standard Gram inverse. No earlier paper is asserted to state the final sampling wording verbatim; the demonstrated mechanical implication, rather than a title match or an access failure, is decisive.

## value

FAIL

The object and spectral question are natural, and the real-incidence proof is a useful exposition. But the frozen contribution is this exact invariant and its rank, tightness and norm readouts, all mechanically implied by the older branching data under standard Fourier diagonalization. No separately stated new structural result or nonroutine surviving quantitative gap remains after crediting that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
