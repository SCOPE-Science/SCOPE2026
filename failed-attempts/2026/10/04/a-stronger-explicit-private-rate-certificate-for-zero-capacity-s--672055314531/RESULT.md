# A stronger explicit private-rate certificate for zero-capacity superactivation
## Finding
For the four-level channel and half-erasure qubit helper introduced in arXiv:2609.10520v1, keep exactly the paper's background state \(\rho_0\), signal state \(\rho_1\), mixed signal letter \(\rho_t=(1-t)\rho_0+t\rho_1\), and fixed binary receiver measurement. Change only the prior probability of the signal letter from \(1/4\) to a general \(q\in(0,1)\). Then every rate below
\[
R_p(q,t)=h_2(q a_p t)-q h_2(a_p t)-pJ_22.77777777777778(q,t)-(1-p)J_4(q,t)
\]
is achievable for \(1/2\le p<1\) and \(0<t\le1/2\), where
\[
a_p=\frac{1-p}7,\qquad
r_s^{(c)}=\frac{1+(c-1)s}c,
\]
and
\[
J_c(q,t)=h_2(r_{qt}^{(c)})-(1-q)h_2(r_0^{(c)})-q h_2(r_t^{(c)}).
\]
Here \(h_2\) is the binary entropy in bits.

At half erasure, the rational choice
\[
q=\frac{39}{200},\qquad t=\frac4{299}
\]
gives the rigorous certificate
\[
R_{1/2}\!\left(\frac{39}{200},\frac4{299}\right)>0.0002101
\]
bits per product use. The published bound for the same channel pair is
\[
\frac{3\ln 2}{10927}\approx0.0001903030605,
\]
so this explicit certificate is more than ten percent larger.

## Assumptions and scope
The channel, its complementary channel, the helper erasure dilation, the three encoding vectors, the two states \(\rho_0,\rho_1\), and the receiver POVM are exactly those of arXiv:2609.10520v1. The environmental domination inequalities used are the paper's
\[
\sigma_1\preceq\frac{205}9\sigma_0,
\qquad
\epsilon_1\preceq4\epsilon_0.
\]
No new assertion is made about the individual zero-private-capacity proofs. The result changes only the binary input prior and uses the paper's direct private coding theorem after the fixed measurement. It is a lower bound for this explicit architecture, not an upper bound and not an exact evaluation of private capacity.

## Proof
Let \(U\in\{0,1}\) have \(\Pr(U=1)=q\). Conditional on \(U=0\), Alice sends \(\rho_0\); conditional on \(U=1\), she sends \(\rho_t=(1-t)\rho_0+t\rho_1\).

The source proves that Bob's fixed click event has probabilities
\[
\Pr(Y=1\mid U=0)=0,
\qquad
\Pr(Y=1\mid U=1)=a_pt,
\qquad a_p=\frac{1-p}7.
\]
Therefore Bob's mutual information is exactly
\[
I(U:Y)=h_2(q a_pt)-q h_2(a_pt).
\]

For Eve, first consider density operators \(\omega_0,\omega_1\) satisfying \(\omega_1\preceq c\omega_0\), with \(c>1\). Set
\[
\tau=\frac{c\omega_0-\omega_1}{c-1},
\qquad
r_s^{(c)}=\frac{1+(c-1)s}c.
\]
Then \(\tau\) is a density operator and, for every \(s\in[0,1]\),
\[
\omega_s=(1-s)\omega_0+s\omega_1
=r_s^{(c)}\omega_1+(1-r_s^{(c)})\tau.
\]
Thus the binary ensemble \(\omega_0,\omega_t\) is obtained by applying one fixed preparation channel to a classical coin whose biases are \(r_0^{(c)}\) and \(r_t^{(c)}\). Data processing therefore gives the exact coin upper bound
\[
\chi(U:E)\le
h_2(r_{qt}^{(c)})-(1-q)h_2(r_0^{(c)})-q h_2(r_t^{(c)})
=J_c(q,t).
\]

The erasure flag is independent of \(U\). The source's full-environment and reduced-environment orders have \(c=205/9\) and \(c=4\), with branch weights \(p\) and \(1-p\). Hence
\[
\chi(U:E'E)\le pJ_{205/9}(q,t)+(1-p)J_4(q,t).
\]
Subtracting this from Bob's exact mutual information proves the displayed bound \(R_p(q,t)\). Repetition of this fixed input ensemble and receiver measurement produces the same memoryless classical-quantum wiretap channel as in the source, so the private coding theorem achieves every rate strictly below \(R_p(q,t)\).

For \(p=1/2\), \(q=39/200\), and \(t=4/299\), all arguments are rational except binary entropy values. The bundled verifier evaluates those entropies with rational interval bounds for logarithms obtained from the convergent identity
\[
\ln y=2\sum_{n\ge0}\frac{z^{2n+1}}{2n+1},
\qquad z=\frac{y-1}{y+1},
\]
after powers-of-two range reduction, and bounds the omitted positive tail geometrically. It proves a lower endpoint above \(0.0002101\).

## Verification
Run `python3 verify.py`. The script uses only the Python standard library and exact rational arithmetic for all algebraic inputs. It prints rigorous lower and upper interval consequences, checks \(t\le1/2\), proves the certified rate exceeds \(0.0002101\), and proves it exceeds \(1.1\) times the published half-erasure bound. Numerical floating-point values printed by the script are display-only conversions of already established rational interval bounds.

## Relationship to prior work
Zhu and Wang prove the first private-capacity superactivation example and use the same states and measurement with fixed priors \(3/4,1/4\). Their Bob bound keeps only a linear click contribution, while their environmental coin lemma further upper-bounds the coin mutual information by a quadratic curvature estimate. The present argument retains Bob's exact binary mutual information and the exact classical-coin mutual information bound, while also freeing the signal prior \(q\). The resulting explicit half-erasure certificate is strictly stronger for the same physical channel pair and measurement architecture.

Targeted searches for the source identifier, the value \(0.0002101\), arbitrary-prior versions of the coin argument, and improved lower bounds found the original \(0.0001903\) certificate and discussions of the same source, but no statement of the bound above.

## Limitations
The certificate does not optimize over all \(q,t\), input ensembles, measurements, block encodings, or decoding strategies. The rational point \(q=39/200\), \(t=4/299\) is chosen only to give a compact reproducible improvement. The result does not determine the exact private capacity and does not characterize other activating zero-private-capacity channels. Originality remains subject to the possibility of an equivalent unpublished or differently phrased optimization not surfaced by the inspected literature.

## References
1. C. Zhu and X. Wang, “Private communication via zero-private-capacity quantum channels,” arXiv:2609.10520v1, 9 September 2026.
2. I. Devetak, “The private classical capacity and quantum capacity of a quantum channel,” IEEE Transactions on Information Theory 51 (2005), 44–55; arXiv:quant-ph/0304127.
3. MSC2020, 81P45, Quantum information, communication, networks.
