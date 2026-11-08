# Exact cyclic image obstructions for two open five-neighbor binary automata

## Finding

Two five-neighbor binary cellular automata, denoted \(F_A\) and \(F_C\), have **complete nonlinear parity tests** for whether a prescribed binary word on a periodic ring has a predecessor. The tests hold for every ring size \(N\geq1\). On each ring exactly \(2^{N-1}\) target words are attainable, each with exactly two predecessors. In contrast to the equal global multiplicities, the two rules have sharply different forbidden sparse patterns: for all \(N\geq7\), every one-marker word is forbidden for \(F_A\) but allowed for \(F_C\); among two-marker targets, precisely the \(N\) pairs at cyclic distance three are forbidden for \(F_A\), whereas precisely the \(2N\) pairs at cyclic distances one or two are forbidden for \(F_C\). Both maps are two-to-one surjections on the bi-infinite full shift. These results do not determine local eventual onto-ness.

## Assumptions and scope

All addition and multiplication in the displayed local Boolean rules take place in \(\mathbb F_2\). Write \((a,b,c,d,e)\) for five consecutive input bits. Define
\[
 f_A(a,b,c,d,e)=b+c+(a+b)\bigl(cd+(c+d+1)e\bigr),
\]
\[
 f_C(a,b,c,d,e)=b+(a+b)(cd+ce+c+de)+c(d+e)+de.
\]
The two rules are the first and third of the three degree-five-neighborhood, two-to-one, non-bipermutive examples in Appendix B of Haugland--Larsen--Omland--Rustad (2026); the subscript is only a label. Let \(F_\nu(x)_i=f_\nu(x_i,x_{i+1},x_{i+2},x_{i+3},x_{i+4})\), \(\nu\in\{A,C\}\), for \(x\in\mathbb F_2^{\mathbb Z}\) or \(x\in\mathbb F_2^{\mathbb Z/N\mathbb Z}\). Indices on a ring are interpreted modulo \(N\), including for \(N<5\). The shift is \((\sigma u)_i=u_{i+1}\), and the difference map is \((Du)_i=u_i+u_{i+1}\). A target is a *Garden-of-Eden ring word* if it has no predecessor under its ring map. Cyclic distance between two distinct positions is the minimum of their clockwise and counterclockwise separations.

Define the explicit parity functionals on periodic target words
\[
 \Phi_{A,N}(y)=\sum_{i\in\mathbb Z/N\mathbb Z}\left[y_i+y_{i-1}(1+y_{i+1})y_{i+2}\right]\pmod2,
\]
\[
 \Phi_{C,N}(y)=\sum_{i\in\mathbb Z/N\mathbb Z}\left[y_i+(1+y_{i-1})y_{i+1}(1+y_{i+2})\right]\pmod2.
\]
For each \(\nu\in\{A,C\}\), every integer \(N\ge1\), and every \(y\in\mathbb F_2^{\mathbb Z/N\mathbb Z}\),
\[
 \boxed{\#F_{\nu,N}^{-1}(y)=\begin{cases}2,&\Phi_{\nu,N}(y)=0,\\0,&\Phi_{\nu,N}(y)=1.\end{cases}}
\]
In particular, the image occupies exactly half the ring, at every \(N\); the assertion includes all short-ring coincidences automatically. For \(N\ge7\), if \(y\) contains exactly one 1 then \(\Phi_{A,N}(y)=1\) and \(\Phi_{C,N}(y)=0\). If \(y\) contains exactly two 1s at cyclic distance \(\delta\), then
\[
 \boxed{\Phi_{A,N}(y)=\mathbf1_{\{\delta=3\}},\qquad
 \Phi_{C,N}(y)=\mathbf1_{\{\delta\in\{1,2\}\}}.}
\]
Therefore the two rules have exactly \(N\) and \(2N\) forbidden two-marker ring words, respectively, for all \(N\ge7\).

## Proof

Set \((H_Au)_i=u_i+u_{i-1}(1+u_{i+1})u_{i+2}\) and \((H_Cu)_i=u_i+(1+u_{i-1})u_{i+1}(1+u_{i+2})\). These maps act on either configuration space. They satisfy
\[
 \boxed{F_A=\sigma H_A D,\quad F_C=\sigma H_C D,\quad H_A^2=H_C^2=\mathrm{id}.}
\]
For the first factorization, write \(p=a+b,q=b+c,r=c+d,s=d+e\). The site \(i+1\) output of \(H_A(Dx)\) is \(q+p(1+r)s\). The Boolean identity \((1+c+d)(d+e)=cd+(1+c+d)e\) gives \(f_A\). For the second factorization, the corresponding site output is \(q+(1+p)r(1+s)\); its expansion agrees term-for-term in \(\mathbb F_2\) with \(f_C\). The two finite Boolean identities can alternatively be checked on all 32 five-bit inputs by the accompanying standalone checker.

The involution identity requires proof rather than an assumption about reversible cellular automata. Put \(t_i(u)=u_{i-1}(1+u_{i+1})u_{i+2}\) and \(v=H_Au\). One has \(t_i(v)=t_i(u)\) at every site. Indeed, write \(a=u_{i-2},b=u_{i-1},c=u_i,d=u_{i+1},e=u_{i+2},f=u_{i+3},g=u_{i+4}\). Then
\[
 t_i(v)=\left[b+a(1+c)d\right]\left[1+d+c(1+e)f\right]\left[e+d(1+f)g\right].
\]
If \(d=0\), this reduces to \(be=t_i(u)\) because \(e(1+e)=0\). If \(d=1\), the middle factor becomes \(c(1+e)f\) and its product with the remaining factors is zero since \(c(1+c)=e(1+e)=f(1+f)=0\); again \(t_i(v)=t_i(u)=0\). Thus applying \(H_A\) twice adds the same trigger twice, giving the identity. For bitwise complement \((Ju)_i=1+u_i\), direct substitution yields \(H_C=JH_AJ\), so \(H_C^2=\mathrm{id}\) as well. These identities are local and remain valid when some indices coincide on short rings.

On a ring, summing \((Dx)_i=x_i+x_{i+1}\) over the sites gives zero. Conversely, for every even-parity word \(z\) choose \(x_0\) freely and integrate \(x_{i+1}=x_i+z_i\) once around the ring; the parity condition closes the cycle. Hence \(\operatorname{im}(D_N)=\{z:\sum_i z_i=0\}\) and each such \(z\) has exactly two predecessors. In the bi-infinite full shift, choose \(x_0\) and integrate in both directions; every \(z\) again has exactly two predecessors, with no parity restriction. Since \(H_\nu\) and \(\sigma\) are bijections and commute with \(\sigma\), the factorization proves the bi-infinite claim and implies that the ring target \(y\) is in the image precisely when \(\sum_i(H_\nu\sigma^{-1}y)_i=0\). Since \(H_\nu\sigma^{-1}=\sigma^{-1}H_\nu\), the latter condition is exactly \(\Phi_{\nu,N}(y)=0\). Invertibility of \(H_\nu\) also shows that this parity functional is balanced, so exactly half of all targets satisfy it.

For \(N\ge7\), a one-marker input has no \(H_A\) trigger: each such trigger requires two separated 1s. Therefore its \(H_A\) parity is one. In \(H_C\), each 1 generates exactly one trigger because the sites two positions before and one after it are zero; the output parity is zero. For exactly two 1s, an \(H_A\) trigger needs them separated by three in one cyclic direction and fires once when that happens (the other direction is distinct for \(N\ge7\)); otherwise none fires. Its original word parity is zero. An \(H_C\) trigger fires at each 1 unless the other 1 lies one position after or two positions before it. If the markers have cyclic distance one or two, exactly one of these two triggers fires. At all larger distances either both fire, or none is suppressed, so the trigger parity is even. The number of pairs at each fixed cyclic distance \(\delta<N/2\) is \(N\). This yields the asserted forbidden two-marker counts.

## Verification

The accompanying `verify.py` uses only the Python standard library. Run `python3 verify.py` from the directory containing this file. It checks every five-bit Boolean identity; every cyclic word on rings of sizes one through ten for the involution, factorization, complement relation, parity image test, and exact fiber multiplicities; and every one-marker and two-marker word on rings of sizes seven through twelve. The extracted script prints `VERIFY_OK checks=15022`. The universal claims rely on the algebraic proof above, not on finite enumeration.

## Relationship to prior work

Haugland, Larsen, Omland and Rustad (2026), Appendix B, **already identify** both five-neighbor rules and prove that their bi-infinite cellular automata are two-to-one. They leave the locally-eventually-onto status of all three two-to-one examples unresolved. The present contribution is the stronger *periodic-target membership formula and sparse Garden-of-Eden geometry* for two of those rules, using an explicit nonlinear reversible dressing of the adjacent-difference map. No claim is made to the prior two-to-one classification or to novelty of the general Boolean landscape involution technique. Haugland and Omland's 2026 papers on reversible cellular automata and almost liftings discuss reversible landscape components, finite cyclic images, and collision/image-size criteria; those general discussions do not by themselves identify these two rules' nonlinear ring-image membership tests or their opposite one-/two-marker behavior. The first rule is not proved LEO here, nor is the third.

## Limitations

The analysis is specific to the displayed first and third five-neighbor rules: it does not classify the second two-to-one rule in the source table, LEO behavior, image geometry of arbitrary open cellular automata, or dynamical iterates. The sparse-pattern statements require \(N\ge7\), whereas the parity membership criterion and exact two-preimage count hold for every \(N\ge1\). Historical priority against a possible unpublished specialized finite-ring image classification remains open; the literature comparison is not an independent audit.

## References

1. J. K. Haugland, N. S. Larsen, T. Omland and H. G. Rustad, *Locally eventually onto cellular automata*, arXiv:2610.33131v1 (first public 2026-10-23), especially Section 3 and Appendix B; https://arxiv.org/abs/2610.33131 .
2. J. K. Haugland and T. Omland, *Shift-invariant transformations and almost liftings*, *Cryptography and Communications* 18 (2026), 705--726; https://doi.org/10.1007/s12095-025-00848-w (preprint available 2024).
3. J. K. Haugland and T. Omland, *New classes of reversible cellular automata*, *Designs, Codes and Cryptography* 94 (2026), article 131; https://doi.org/10.1007/s10623-026-01869-z (preprint arXiv:2411.00721).
