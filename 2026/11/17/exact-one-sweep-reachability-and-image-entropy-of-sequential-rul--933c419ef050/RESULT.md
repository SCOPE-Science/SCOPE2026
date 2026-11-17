# Exact one-sweep reachability and image entropy of sequential Rule 30

## Finding

Let \(n\ge 3\). On a labelled, periodic binary ring, update sites \(0,1,\ldots,n-1\) once, in that order and in place, with the Rule 30 local map \(f(l,c,r)=l\oplus(c\lor r)\). If \(I_n\) is the number of distinct resulting binary words, then
\[
\sum_{n\ge3} I_nz^n=\frac{z^3(4+2z^2+z^3)}{1-2z+z^2-z^3}.
\]
In particular the first values, at ring lengths \(3,4,\ldots,12\), are \(4,8,14,25,44,77,135,237,416,730\). The image growth rate is \(\lambda=1.75487766624669\ldots\), the unique real root greater than one of \(\lambda^3-2\lambda^2+\lambda-1=0\). More precisely,
\[
I_n\sim 0.855744425268871\ldots\,\lambda^n,
\qquad \lim_{n\to\infty}\frac{\log_2 I_n}{n}=0.811370462751649\ldots.
\]
A constructive, boundary-sensitive criterion decides reachability of **every** output word and supplies a predecessor when one exists.

## Assumptions and scope

All bits are in \(\{0,1\}\), \(\oplus\) is addition modulo two, and \(\lor\) is Boolean disjunction. Distinct sites are labelled; configurations are not identified under rotation or complementation. Cyclic neighbors are taken modulo \(n\). The scan is deterministic, single-pass, and in place: when site \(i\) is updated, previously updated sites already carry their new value, and sites not yet visited carry their old value. These statements concern **one** scan, not synchronous updates, long-time attractors, or random update orders.

For output \(y=(y_0,\ldots,y_{n-1})\), define \(d_i=y_{i-1}\oplus y_i\) for \(1\le i\le n-1\). Define Boolean relation matrices
\[
E_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
E_1=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad
P=E_{d_1}\odot E_{d_2}\odot\cdots\odot E_{d_{n-2}},
\]
where \(\odot\) denotes Boolean matrix multiplication (OR of ANDs). Then \(y\) is reachable **if and only if** one of the following mutually exclusive tests succeeds:

* \(y_0=0\), \(d_{n-1}=0\), and \(P_{00}=1\);
* \(y_0=0\), \(d_{n-1}=1\), and \(P_{01}\lor P_{11}=1\);
* \(y_0=1\), \(d_{n-1}=1\), and \(P_{00}\lor P_{01}\lor P_{10}=1\).

If \(y_0=1\) and \(d_{n-1}=0\), no predecessor exists.

## Proof

**1. Reduction to one-dimensional endpoint relations.** Let \(x=(x_0,\ldots,x_{n-1})\) be a putative predecessor. The in-place rule yields
\[
\begin{aligned}
y_0&=x_{n-1}\oplus(x_0\lor x_1),\\
y_i&=y_{i-1}\oplus(x_i\lor x_{i+1})\qquad(1\le i\le n-2),\\
y_{n-1}&=y_{n-2}\oplus(x_{n-1}\lor y_0).
\end{aligned}
\]
Consequently \(d_i=x_i\lor x_{i+1}\) for interior indices, and \(d_{n-1}=x_{n-1}\lor y_0\). Since \((E_e)_{ab}=1\) precisely when \(a\lor b=e\), the relation \(P_{ab}=1\) is equivalent to an interior path \(x_1=a,\ldots,x_{n-1}=b\) with these prescribed differences.

For given endpoints \((a,b)\), the first update can be met exactly when \(x_0\lor a=y_0\oplus b\). If \(y_0=0\), this demands \(a\le b\), and the final equation demands \(d_{n-1}=b\). If \(y_0=1\), the first equation demands \((a,b)\ne(1,1)\), and the final equation demands \(d_{n-1}=1\). These are precisely the three tests stated above. Conversely, every passing path supplies the explicit first bit \(x_0=y_0\oplus b\), and all resulting updates agree with \(y\), proving sufficiency and constructive inversion.

**2. Finite relation monoid and exact enumeration.** For any Boolean relation \(P\) define
\[
w(P)=P_{00}+(P_{01}\lor P_{11})+(P_{00}\lor P_{01}\lor P_{10}),
\]
with disjunction values treated as zero or one. For each fixed interior difference string, \(w(P)\) is exactly the number of admissible pairs \((y_0,d_{n-1})\). The transformation \(y\mapsto (y_0,d_1,\ldots,d_{n-1})\) is bijective, so every output is counted exactly once.

Starting from the identity relation and repeatedly right-multiplying by \(E_0\) or \(E_1\) reaches exactly 12 Boolean matrices. Their complete multiplication table is below; a state is encoded by the four entries \((P_{00},P_{01},P_{10},P_{11})\), each pair lists transitions under \(E_0,E_1\), and the final number is \(w(P)\):

```text
00 1001 -> (01,02), weight=3
01 1000 -> (01,03), weight=2
02 0111 -> (04,05), weight=2
03 0100 -> (06,07), weight=2
04 0010 -> (04,08), weight=1
05 1111 -> (09,05), weight=3
06 0000 -> (06,06), weight=0
07 1100 -> (01,07), weight=3
08 0001 -> (06,10), weight=1
09 1010 -> (09,11), weight=2
10 0011 -> (04,10), weight=2
11 0101 -> (06,05), weight=2
```

Let \(T\) be the integer transition matrix defined by this table: \(T_{ij}\) is the number (zero, one or two) of labelled choices \(e\in\{0,1\}\) taking state \(i\) to state \(j\). Let \(w\) be the displayed weight column and \(e_0\) the first coordinate column. The exact image count is
\[
I_n=e_0^{\mathsf T}T^{n-2}w\qquad(n\ge3).
\]
Direct multiplication of the displayed 12-state table gives the **full integer vector identity**
\[
T^2(T^3-2T^2+T-I)w=0.
\]
The standalone arithmetic checker reproduces every table entry and verifies all 12 components of this identity without floating-point arithmetic. Thus \(I_{n+3}=2I_{n+2}-I_{n+1}+I_n\) for all \(n\ge4\). The initial values from the table are \(I_3=4\), \(I_4=8\), \(I_5=14\), and \(I_6=25\), yielding the stated rational generating function, including its length-three boundary correction.

**3. Asymptotic law.** The denominator \(D(z)=1-2z+z^2-z^3\) has one positive real root \(\rho=0.569840290998053\ldots\), and its other roots have larger modulus. Equivalently the characteristic cubic has a unique real root \(\lambda=1/\rho>1\); its other two roots have modulus \(\lambda^{-1/2}<1\) by their conjugacy and the product-of-roots identity. The numerator does not vanish at \(\rho\). The simple-pole expansion proves
\[
I_n\sim -\frac{\rho^3(4+2\rho^2+\rho^3)}{\rho D'(\rho)}\rho^{-n}
=0.855744425268871\ldots\,\lambda^n.
\]
This also establishes the stated binary image entropy and the exponentially vanishing fraction \(I_n/2^n\).

## Verification

Run `python3 verify_relation.py` for the independent construction of the relation monoid, its complete table and exact 12-component matrix identity. Run `python3 verify_direct.py` for a separate in-place simulator: it enumerates all inputs for each \(3\le n\le16\), checks exact image counts, and for all \(3\le n\le12\) independently enumerates all outputs, builds a predecessor using the constructive criterion, and checks the images coincide. Both use only Python's standard library. Their recorded outputs are included as `relation_output.txt` and `direct_output.txt`. The symbolic matrix identity and proof, not the finite simulations alone, establish the all-length result.

## Relationship to prior work

Wolfram's 1983 cellular-automaton study established the elementary local-rule setting and analyzed simultaneous updates. Macauley, McCammond and Mortveit's study of asynchronous elementary automata establishes a general sequential-update framework, but its principal classification concerns independence of recurrent sets from update order. Wong's 2025 investigation includes illustrations of sequential Rule 30 and studies branching, small-parameter sequential systems; its reported investigations do not give an all-length exact one-pass cyclic image census. Synchronous Rule 30 predecessor enumerations address a different global map and are not interchangeable with an in-place sweep. The result here counts **distinct outputs**, not trajectories or input multiplicities.

## Limitations

The theorem is for a fixed labelled cycle and the specified left-to-right sequential order. Rotating the order along with the labels gives an equivalent scan, but arbitrary permutations, synchronous updates, random update orders, open boundaries, repeated sweeps, and temporal attractor classifications are not asserted. Finite checks stop at length sixteen; all-length conclusions depend on the displayed relation-monoid proof. This study does not establish exclusive historical priority over inaccessible or unindexed literature.

## References

1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644. https://doi.org/10.1103/RevModPhys.55.601 (published 1983-07-01).
2. M. Macauley, J. McCammond, H. S. Mortveit, *Order Independence in Asynchronous Cellular Automata*, arXiv:0707.2360 (first version 2007-07-16). https://arxiv.org/abs/0707.2360.
3. M. H. Wong, *Multiway Sequential Cellular Automata*, Complex Systems **34** (2025), 325–372. https://doi.org/10.25088/ComplexSystems.34.3.325.
