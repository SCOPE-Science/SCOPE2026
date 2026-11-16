# Sharp Walsh gaps and the first nontrivial nullity for binary-tree independent sets

## Finding

Let \(B_h\) be the complete rooted binary tree of height \(h\geq0\), with \(2^{h+1}-1\) vertices, and let \(f_h:\mathbb F_2^{V(B_h)}\to\{0,1\}\) be the indicator of independent vertex sets. Define the **unnormalized** Walsh multiplier and its nonzero gap by
\[
W_h(s)=\sum_{x\in\mathbb F_2^{V(B_h)}} f_h(x)(-1)^{\sum_v s_vx_v},\qquad
\delta_h=\min_{s:W_h(s)\ne0}|W_h(s)|.
\]
The following sharp gap law holds at **every** height:
\[
\boxed{\delta_h=\begin{cases}2,&h\equiv0\pmod3,\\1,&h\equiv1,2\pmod3.\end{cases}}
\]
In particular, on the group \(G_h=\mathbb F_2^{V(B_h)}\), counting convolution \(T_hg=f_h*g\) has exact Hilbert-space Moore--Penrose inverse norm
\[
\boxed{\|T_h^\dagger\|_{\ell^2(G_h)\to\ell^2(G_h)}=\delta_h^{-1}}.
\]
There are no zero multipliers for \(h\equiv1,2\pmod3\); for \(h\equiv0\pmod3\), zero and nonzero multipliers both exist. The invertibility residue criterion also follows from previous results about the independence polynomial at \(-1\) and is not asserted as a new priority claim.

The **first nontrivial singular height**, \(h=3\), has \(15\) vertices, \(2306\) independent sets and exactly
\[
\boxed{14402=120^2+2}
\]
zero Walsh multipliers among its \(32768\) characters. Thus \(\operatorname{rank}T_3=18366\). All zero characters have negative root sign. Exactly \(120^2\) of them arise by choosing in both height-two descendant subtrees a character whose total and root-excluded signed sums coincide; the remaining **two** arise by pairing the unique two descendant characters with reciprocal ratios \(9/25\) and \(25/9\), in either order. This completely classifies the first nontrivial zero set.

## Assumptions and scope

The tree has labelled vertices equal to binary words of lengths \(0,\ldots,h\), with the empty word at the root and an edge from each nonleaf to its two children. An independent set contains no adjacent pair. The empty set is included. The Fourier transform is a *counting*, not probability-normalized, transform on the full Boolean coordinate group. No uniform distribution on characters is assumed in the analytic claims. In the singular case the pseudoinverse acts as zero on the Fourier nullspace, and the norm is taken on the full counting \(\ell^2\) space.

For any frequency \(s\), let \(F_h(s)=W_h(s)\), and let \(E_h(s)\) be the signed sum over independent sets omitting the root. If \(s=(r,s_L,s_R)\), where \(r\) is its root bit, then
\[
E_h(s)=F_{h-1}(s_L)F_{h-1}(s_R),\qquad
F_h(s)=E_h(s)+(-1)^r E_{h-1}(s_L)E_{h-1}(s_R).
\]
At height zero, \((F_0(0),E_0(0))=(2,1)\), and \((F_0(1),E_0(1))=(0,1)\).

## Proof

**1. Uniform parity obstruction.** Set \(q_h=F_h(0)\), the total number of independent sets. Conditioning on the root gives \(q_0=2\), \(q_1=5\), and for \(h\ge2\),
\[
q_h=q_{h-1}^{\,2}+q_{h-2}^{\,4}.
\]
Because all signs are \(1\) modulo \(2\), every \(F_h(s)\) is congruent to \(q_h\pmod2\). The recurrence modulo two reduces to \(q_h\equiv q_{h-1}+q_{h-2}\pmod2\), giving the repeating residues \(0,1,1\) at heights \(0,1,2\). Hence every multiplier is odd for heights \(1,2\pmod3\), and every multiplier is even at heights \(0\pmod3\). Nonzero magnitudes are therefore at least \(1\) and \(2\), respectively.

**2. Exact attaining characters.** Construct one character recursively by giving *both* height-\((h-1)\) subtrees the previously constructed character. Begin with frequency \(1\) on the one-vertex tree, yielding \((F_0,E_0)=(0,1)\). Choose the root frequency bit \(r=0,0,1\) in successive height classes \(1,2,0\pmod3\). The displayed state recurrence yields the exact three-cycle
\[
(0,1)\xrightarrow{r=0}(1,0)\xrightarrow{r=0}(1,1)\xrightarrow{r=1}(0,1).
\]
Thus at every height \(1,2\pmod3\) there is a multiplier \(1\), while at every height \(0\pmod3\) there is a zero multiplier. Also, for \(h\ge3\) divisible by three, use both descendant characters of state \((1,1)\) but choose \(r=0\), obtaining \((F_h,E_h)=(2,1)\). At \(h=0\), the trivial character has multiplier \(2\). Therefore the parity lower bounds in Step 1 are attained at every height, proving the sharp gap law.

**3. Exact first nontrivial nullity.** At height one there are eight frequencies with the following state multiplicities:
\[
(-1,0):3,\quad(1,0):3,\quad(3,4):1,\quad(5,4):1.
\]
Pair these states independently to obtain the height-two frequency states by the recurrence, with either root sign. Among \(128\) height-two frequencies, the ratio \(F_2/E_2\) is always defined, because \(E_2\) is an odd product of height-one totals. Its *complete* ratio multiplicity table is:

| Ratio \(F_2/E_2\) | Multiplicity |
|---|---:|
| \(1\) | 120 |
| \(-7/9\) | 1 |
| \(25/9\) | 1 |
| \(9/25\) | 1 |
| \(41/25\) | 1 |
| \(-1/15\) | 2 |
| \(31/15\) | 2 |

At height three, the multiplier vanishes if and only if
\[
\frac{F_2(s_L)}{E_2(s_L)}\frac{F_2(s_R)}{E_2(s_R)}=-(-1)^r.
\]
Inspection of the **complete seven-ratio list** shows that no ordered pair has product \(-1\). The pairs with product \(+1\) are the \(120^2\) ordered choices of ratio \(1\), plus the two ordered cross-pairs of ratios \(25/9\) and \(9/25\). Hence the root bit must be \(1\), and the number of vanishing frequencies is exactly \(120^2+2=14402\). Since \(|G_3|=2^{15}=32768\), Fourier diagonalization yields the claimed rank \(18366\).

**4. Exact stability.** The Walsh characters are an orthogonal basis for counting \(\ell^2(G_h)\). On each character, counting convolution by \(f_h\) is multiplication by \(F_h(s)\). Thus its Moore--Penrose inverse has norm \(1/\min_{F_h(s)\ne0}|F_h(s)|\), as asserted. The largest absolute multiplier equals \(q_h\), achieved at the trivial character; consequently the positive-spectrum condition number is exactly \(q_h/\delta_h\).

## Verification

Run `python3 tree_walsh_check.py` and `python3 tree_state_certificate.py` with Python 3 and the standard library. The first program builds **all** independent-set incidence vectors of \(B_h\) for \(0\le h\le3\), performs a full integer fast Walsh--Hadamard transform, and compares **every** coefficient with an independently implemented signed root recurrence. It checks \(2306\) independent sets, \(32768\) characters, the \(14402\) zeros, rank \(18366\), the sharp gap, the exact Parseval sum \(32768\cdot2306\), and the explicit three-cycle witness. The second program separately builds integer state multiplicity dictionaries and the seven-ratio cancellation certificate; it checks \(120^2+2\) by root sign and the same Parseval identity. Both return explicit PASS markers.

The finite programs are verification of the complete \(h=3\) census and examples. The infinite-height gap and inverse-norm assertions are proved by the parity recurrence and three-cycle construction, **not** by extrapolating finite enumeration.

## Relationship to prior work

The standard deletion recurrence for independence polynomials is classical and appears in Levit--Mandrescu [1] and Trinks [2]. Levit--Mandrescu's result that the independence polynomial of *any* tree at homogeneous activity \(-1\) belongs to \(\{-1,0,1\}\), together with the elementary count-parity recurrence, already implies the binary-tree **invertibility residue criterion**. No novelty is assigned to that criterion alone. A related published mathematical treatment of full rooted-tree independence complexes [3] also gives a three-height cycle for homogeneous signed independence counts, but concerns topological homology representations, not all inhomogeneous Boolean characters.

The contribution here is the sharp **all-character nonzero Walsh gap and pseudoinverse norm at every height**, together with the complete first nontrivial Fourier nullity and the two exceptional reciprocal state-ratio cancellations. The general graph-exclusion Fourier *principal submatrix* invertibility theorem [4] uses a different operator indexed only by independent sets, rather than convolution on the full Boolean group; it does not imply the convolution spectral zeros or sharp norm here.

## Limitations

The exact nullity enumeration is for height three; a general nullity formula for larger multiples of three is not proved. The spectral gap and invertibility classification apply to full binary trees with exactly two children per nonleaf, not arbitrary branching patterns or arbitrary trees. The \(\ell^2\) pseudoinverse norm is for unnormalized counting convolution; probability normalization rescales all multipliers. The comparisons were bounded and do not exclude unindexed historical calculations or unpublished exact tables. No independent mathematical audit is claimed.

## References

1. V. E. Levit and E. Mandrescu, *The independence polynomial of a graph at -1*, arXiv:0904.4819v1, 30 April 2009, especially Theorem 2.4 and the deletion recurrence. https://arxiv.org/abs/0904.4819
2. M. Trinks, *A survey on recurrence relations for the independence polynomial of hypergraphs*, arXiv:1406.2990v1, 11 June 2014, Sections 1, 3 and 4. https://arxiv.org/abs/1406.2990
3. *Orientation characters of independence-complex spheres of full rooted trees*, published mathematical record dated 18 October 2026; its recurrence for homogeneous signed counts and nonequivariant sphere classification are distinguished from the all-character problem here.
4. *Graph-exclusion Fourier interpolation: universal invertibility and a mod-four inverse resonance*, published mathematical record dated 8 November 2026; the principal Fourier submatrix indexed by independent supports is a distinct object.
