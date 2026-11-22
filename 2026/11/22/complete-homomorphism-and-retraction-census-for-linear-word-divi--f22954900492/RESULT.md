# Complete homomorphism and retraction census for linear-word divisibility semirings

## Finding
For all integers \(k,m\ge1\), the complete homomorphism set between the linear-word divisibility-order ai-semirings \(S_k=S_c^*(a_1\cdots a_k)\) and \(S_m\) has the natural disjoint-block model
\[
\operatorname{Hom}(S_k,S_m)\ \longleftrightarrow
\{(B_1,\ldots,B_k):B_i=0\text{ or }\varnothing\ne B_i\subseteq[m],\ B_i\cap B_j=\varnothing\text{ when }i\ne j\text{ and both nonzero}\}.
\]
Consequently,
\[
|\operatorname{Hom}(S_k,S_m)|=(k+1)^m,
\qquad
H_{k,m}(z)=\sum_{s=0}^{\min(k,m)}\binom ks
\left[\sum_{j=0}^s(-1)^j\binom sj(s+1-j)^m\right]z^s.
\]
The coefficient of \(z^s\) counts homomorphisms whose image has exactly \(2^s\) elements. All kernels are determined by which input letters have zero image: precisely \(\binom ks\) kernels arise with image size \(2^s\). There are surjective homomorphisms \(S_k\twoheadrightarrow S_m\) if and only if \(k\ge m\), and their number is \(k!/(k-m)!\).

For each \(k\ge1\), every composition-idempotent endomorphism of \(S_k\) fixes an arbitrary chosen set of generator singletons and sends all other singletons to \(0\). Thus these retractions form the Boolean meet-semilattice under composition,
\[
P_UP_V=P_{U\cap V},\qquad \#\{P:P^2=P\}=2^k,
\qquad\operatorname{Aut}(S_k)\cong\mathfrak S_k.
\]
The image of \(P_U\) is canonically isomorphic to \(S_{|U|}\) when \(U\ne\varnothing\) and is the one-element semiring when \(U=\varnothing\).

## Assumptions and scope
The signature consists of two binary operations \((+,\cdot)\), without named constants. Identify each nonempty squarefree commutative subword of \(a_1\cdots a_k\) with its nonempty letter support \(I\subseteq[k]\), and adjoin one element \(0\), not identified with the empty subset. For nonzero \(I,J\), define
\[
I+J=I\cup J,\qquad
I\cdot J=\begin{cases}I\cup J,&I\cap J=\varnothing,\\0,&I\cap J\ne\varnothing.\end{cases}
\]
Set \(0+x=x+0=0\) and \(0\cdot x=x\cdot0=0\). Thus \(0\) is *absorbing* for both operations, not an additive identity. This is the linear-word specialization of the divisibility-order construction; it is **not** the distinct flat-addition semiring \(S_c(a_1\cdots a_k)\). Every element squares multiplicatively to \(0\). Homomorphisms preserve both binary operations; retractions are maps \(P\) with \(P^2=P\) under composition. The claims hold for all positive source and target ranks and use labelled generators.

## Proof
**1. Normal form.** Put \(e_i=\{i\}\). Since \(e_i\cdot e_i=0\) and every target element has multiplicative square \(0\), any homomorphism obeys \(f(0)=f(e_i\cdot e_i)=f(e_i)^2=0\). Let \(B_i=f(e_i)\). For distinct \(i,j\), the source identity \(e_i+e_j=e_i\cdot e_j=\{i,j\}\) forces \(B_i+B_j=B_i\cdot B_j\). Two nonzero target supports satisfy this equality exactly if they are disjoint. (If either is \(0\), both sides equal \(0\).) Necessity follows.

Conversely, choose any tuple with the stated pairwise disjointness. For nonempty \(I\subseteq[k]\), define \(f(I)=0\) if any \(B_i=0\) with \(i\in I\), and otherwise \(f(I)=\bigcup_{i\in I}B_i\); define \(f(0)=0\). Union makes it preserve addition, including cases yielding the absorbing \(0\). For multiplication, when \(I\cap J\ne\varnothing\) and neither image vanishes, the two resulting unions share at least one nonempty block and hence multiply to \(0\); if \(I\cap J=\varnothing\), their nonvanishing unions are disjoint and multiply to the union. Vanishing images are absorbed in either case. Therefore the formula preserves both operations. It is unique because \(I=\sum_{i\in I}e_i\) and the \(e_i\) generate the entire semiring. This proves the bijection.

**2. Counting and image sizes.** View each target letter \(j\in[m]\) as assigned to exactly one of \(k\) labelled source blocks or an unused box. Each assignment gives a unique admissible tuple and conversely, so there are \((k+1)^m\) homomorphisms. Let \(T=\{i:B_i\ne0\}\), with \(|T|=s\). Their disjoint nonempty blocks yield exactly \(2^s-1\) nonzero unions plus \(0\), so the image has \(2^s\) elements. Fixing \(T\) and applying inclusion-exclusion to ensure its \(s\) boxes are all occupied gives \(\sum_{j=0}^s(-1)^j\binom sj(s+1-j)^m\), and choosing \(T\) gives the rank polynomial. The kernel identifies \(0\) with precisely those nonzero \(I\) containing a letter outside \(T\), while different nonempty \(I\subseteq T\) have distinct images. Hence exactly one kernel per \(T\), and \(\binom ks\) kernels for each image size. In a surjection, \(2^s=2^m\) forces \(s=m\); then \(m\) disjoint nonempty blocks partition \([m]\) and must all be singletons. Choosing the \(m\) active source positions and their bijection onto \([m]\) yields the falling factorial. Injective homomorphisms correspond exactly to \(s=k\), possible if and only if \(k\le m\).

**3. Idempotents and automorphisms.** For an endomorphism \(f:S_k\to S_k\) with \(f^2=f\), let \(T=\{i:B_i\ne0\}\), \(|T|=s\). For any \(i\in T\), the equality \(f(B_i)=B_i\ne0\) implies \(B_i\subseteq T\): an inactive letter inside \(B_i\) would force \(f(B_i)=0\). The \(s\) pairwise disjoint nonempty sets \(B_i\) are subsets of the \(s\)-element set \(T\), so each is a singleton and together they exhaust \(T\). Their assignment is a permutation of \(T\); the identity \(f^2=f\) makes that permutation idempotent and hence the identity. Thus \(B_i=\{i\}\) for \(i\in T\), and \(B_i=0\) otherwise. Conversely these maps plainly satisfy \(f^2=f\), and composing two deletes all letters outside the intersection. An automorphism must have \(s=k\), so all its generator images are singleton blocks permuting \([k]\); conversely all such permutations act as automorphisms. No other endomorphism is invertible.

## Verification
The standalone \(\texttt{verify.py}\) uses only the Python standard library. Independently of the disjoint-block parametrization, it exhaustively enumerates **all functions** between the respective carriers for \((k,m)=(1,3),(2,2),(2,3),(3,2)\), retains precisely the functions respecting both operation tables, and checks every survivor has the predicted normal form and count. It also independently enumerates all admissible block tuples for every \(k=m\) from \(1\) through \(5\), checking the homomorphism property, exact image-size distributions, idempotents and automorphisms. Running \(\texttt{python3 verify.py}\) prints \(\texttt{VERIFY_OK}\). The all-rank theorem rests on the proof, not on these finite tests.

## Relationship to prior work
Gao (2026), Section 4, defines the divisibility-order family and proves it lies in a particular ai-semiring variety, using it to study continuum-sized subvariety intervals. Shao and Gao (2026) study finite basis properties and joins for the same family. Neither inspected statement provides this complete cross-rank homomorphism and image-kernel classification. A previous treatment of **flat-addition, noncommutative interval-word** semirings concerns different operations and does not imply the block-label formula for the present commutative divisibility-order family. Generic endomorphism and retraction results for other finite semirings likewise do not imply this theorem. Classical inclusion-exclusion is used for the final numerical count but not claimed as new.

## Limitations
The theorem concerns these *particular finite linear-word divisibility-order* semirings and homomorphisms of their binary signature, not arbitrary commutative-word ideals, noncommutative words, flat-addition semirings, or constant-preserving maps in a different signature. It classifies the homomorphism sets, image sizes, kernels, and endomorphism idempotents, not arbitrary congruences. Small finite verifications cannot establish the infinite result without the proof. Literature and indexed database searches cannot prove historical novelty; broader unpublished results may exist.

## References
1. Zidong Gao, *A finitely based finite semiring generates a variety with continuum many subvarieties*, arXiv:2603.00893v1, first publicly available 2026-03-01, especially Section 4. https://arxiv.org/abs/2603.00893
2. Xiaolei Shao and Zidong Gao, *Finite bases and joins for semirings defined by the divisibility order*, arXiv:2609.26396v1, first publicly available 2026-09-22. https://arxiv.org/abs/2609.26396
