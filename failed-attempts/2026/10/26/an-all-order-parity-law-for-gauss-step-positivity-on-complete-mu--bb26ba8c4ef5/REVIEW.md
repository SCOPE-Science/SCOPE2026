# Independent mathematical audit

## correctness

PASS

For s>=1 write Q_s(z)=E_s(z^2)+zO_s(z^2), with positive present coefficients in both parts. The adjacent even-to-odd ratio (2j+1)(2s-2j)/(s-2j) increases, including the terminal unpaired even term by padding O with zero. Thus in E'_s O_s-E_s O'_s every paired coefficient contribution (i-j)(e_i o_j-e_j o_i) is nonnegative. Consequently g_s(z)=2/(z+E_s(z^2)/O_s(z^2)) is positive and strictly decreasing even when the quotient is constant. The spectrum splits into constants, part-wise constants with global sum zero (eigenvalue N), and zero-sum vectors in part i (eigenvalue q_i=N-n_i). This gives cross-part entries h g_s(Nh) and within-part off-diagonal entries q_i h/n_i times [g_s(q_i h)-g_s(Nh)]; singleton parts cause no exception. The binomial/Gamma identity for Q_s makes Q_s(-z)>0 for even s, giving positive eigenvalues and diagonals, and the constant eigenvector plus symmetry gives double stochasticity. For odd s the nonconstant spectral factors tend to -1, giving diagonal limit 2/N-1. When N=2, the entries are (1±R_s(2h))/2, both positive at h>0 since E_s,O_s are positive. At h=0 the map is the identity. This proves the endpoint statement for connected graphs with at least two nonempty parts, no claim about internal stages. The uploaded finite test and output were inspected, not used as an all-order certificate.

## originality

FAIL

Direct equivalent coverage, not an access failure or title match: the distinct indexed record 2026/11/8/SCOPE-stage-parity-classification-of-gauss-legendre-positivity-on-comp--6250aee1370d gives the same all-stage endpoint classification on exactly the same graph family, including every off-diagonal at h>0, the two-vertex exception and eventual negative diagonals. It even uses the same coefficient-ratio divided-difference lemma and the same spectral entry formulas. The different elementary integral representation for the scalar numerator sign is not a distinct theorem of the Finding. The comparison establishes coverage in the published corpus, not priority, direction of dependence, or which derivation was reached first.

## value

PASS

As a theorem, the exact all-order classification on this natural graph family has substantive numerical-analysis content: it separates strict transport off the diagonal from the eventual odd-stage diagonal obstruction and explains the exceptional two-vertex graph. This scientific interest is separate from novelty; a different elementary integral for one scalar sign step is not a surviving, independently valuable new finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
