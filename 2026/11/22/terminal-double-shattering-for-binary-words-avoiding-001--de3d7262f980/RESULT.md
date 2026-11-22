# Terminal-double shattering for binary words avoiding \(001\)

## Finding

For every integer \(n\ge1\), let \(\mathcal A_n\subseteq\{0,1\}^n\) be the entire language of binary words with no consecutive factor \(001\). Regard each word as a Boolean concept on its labeled coordinate positions \([n]\). A support \(S\subseteq[n]\) is *shattered* when every assignment of zeros and ones to its positions extends to at least one word in \(\mathcal A_n\).

**Complete support classification.** A support is shattered if and only if it contains no three positions \(i,i+1,j\) with \(j>i+1\). Equivalently, its selected positions either form an independent set in the path \(P_n\), or comprise an independent set of positions preceding a single terminal adjacent selected pair (all earlier selected positions are separated from that pair by at least one unselected position).

Let \(I_m(z)\) count independent vertex sets of \(P_m\), with \(I_{-1}(z)=I_0(z)=1\), \(I_1(z)=1+z\), and \(I_m(z)=I_{m-1}(z)+zI_{m-2}(z)\) for \(m\ge2\). The full shattered-support polynomial is
\[
\boxed{\Phi_n(z)=I_n(z)+z^2\sum_{t=2}^n I_{t-3}(z)\quad (n\ge1),}
\]
where the empty sum is zero. Consequently, its rational two-variable generating function, including \(\Phi_0=1\), is
\[
\boxed{\sum_{n\ge0}\Phi_n(z)u^n=\frac{1+zu}{1-u-zu^2}+\frac{z^2u^2}{1-u}+\frac{z^2u^3(1+zu)}{(1-u)(1-u-zu^2)}.}
\]
The exact VC dimension for every \(n\ge1\) is
\[
\boxed{\operatorname{VCdim}(\mathcal A_n)=\left\lfloor\frac n2\right\rfloor+1.}
\]
For instance \(\Phi_8(z)=1+8z+28z^2+35z^3+15z^4+z^5\).

## Assumptions and scope

The factor \(001\) is forbidden as a contiguous, linearly ordered triple, not cyclically; the language contains *all* such length-\(n\) words, not the factors of one fixed infinite sequence. Coordinate shattering allows the completion outside the support to depend on the assignment. Supports are labeled subsets, not translation or reversal classes. The statement concerns static VC shattering, not adaptive or Littlestone dimension.

## Proof

**Necessity.** If \(S\) contains \(i,i+1,j\) with \(j>i+1\), prescribe zeros at \(i,i+1\) and a one at \(j\). Every word avoiding \(001\) has the following elementary closure property: whenever two consecutive positions are zero, every subsequent position must be zero. Indeed the immediately following position cannot be one; inductively the next positions are forced zero. The prescribed partial word therefore has no permitted completion. Thus no such support is shattered.

**Sufficiency.** If \(S\) contains no adjacent positions, any prescribed labeling extends by filling all unqueried positions with ones: two adjacent zeros cannot occur, so \(001\) is absent. If \(S\) does contain adjacent positions, let \(i,i+1\) be the first selected adjacent pair. By the assumed support condition, all other selected positions must lie strictly before \(i\); in fact none can be \(i-1\), since this would give the forbidden selected triple \(i-1,i,i+1\). The earlier selected positions have no adjacent pair, since that would precede \(i,i+1\). For any labeling of \(S\), fill all unqueried positions through \(i+1\) with ones, and fill positions after \(i+1\) with zeros only when the two tested positions \(i,i+1\) have both been assigned zero; otherwise fill them with ones. Before the terminal selected pair, no adjacent zeros arise. If the terminal pair is \(00\), the entire later suffix is zero, so \(001\) still cannot arise. In every case the prescribed labeling extends. This proves the characterization for all \(n\), including the short vacuous cases.

**Exact face polynomial.** The supports without adjacent selected positions are exactly the independent sets of \(P_n\), counted by \(I_n(z)\). Any other shattered support has a unique terminal adjacent selected pair \(t-1,t\), with \(2\le t\le n\). All its earlier selected positions lie in \(\{1,\ldots,t-3\}\) and have no adjacent positions. They contribute \(I_{t-3}(z)\), and the terminal pair contributes \(z^2\). These families are disjoint. Summing proves the face polynomial. The standard path-independent-set recurrence gives the generating function \(I(u,z)=(1+zu)/(1-u-zu^2)\); summing the terminal-pair contributions \(z^2\sum_{n\ge0}u^n\sum_{t=2}^n I_{t-3}(z)\) gives \(z^2u^2/(1-u)+z^2u^3I(u,z)/(1-u)\), as displayed.

**Dimension.** The largest independent set in \(P_n\) has \(\lceil n/2\rceil\) positions. A terminal-pair support has at most \(2+\lceil(n-3)/2\rceil\) selected positions for \(n\ge3\), attained by taking its pair in the final two coordinates and a maximum independent set among the first \(n-3\). For \(n\ge3\) the larger of the two expressions is \(\lfloor n/2\rfloor+1\). Directly \(\Phi_1=1+z\), \(\Phi_2=(1+z)^2\), giving the same formula at lengths one and two. \(\square\)

## Verification

Run `python3 verify.py` using only the Python standard library. The checker independently enumerates all \(001\)-avoiding binary words and every possible query support for each length \(1\le n\le12\), directly calculates every support's set of binary traces, and checks the structural criterion and complete face polynomial independently. It passed all 8,190 support decisions and verified the claimed VC dimensions. This is finite corroboration, not the proof of the all-length theorem.

## Relationship to prior work

Johnson's *Binary strings of finite VC dimension* (2021) examines the VC dimension associated to the substring family of an individual binary string, including variants for equal-length factors. The current class instead consists of **all** words avoiding one fixed contiguous factor. The published result *A regular shattering complex for binary words with no monochromatic triple* analyzes the different language avoiding both \(000\) and \(111\): its support obstructions and rational series are different, although its scalar VC dimension happens to agree. The published result *A three-phase sharp Walsh stability law for binary words avoiding \(001\)* studies exactly the present language but its Walsh multipliers, not support shattering. Its automaton-based word count is prior work and is not claimed new. The new content here is the all-support terminal-double criterion, complete shattering polynomial and rational generating function for this one asymmetric forbidden factor.

## Limitations

No claim is made for other forbidden factors beyond the reversal and bit-complement images of \(001\), for cyclic avoidance, or for online shattering. The structural argument uses the special absorbing all-zero suffix of the forbidden factor \(001\) and does not extend unchanged to arbitrary forbidden substrings. Exact prior historical priority is only assessed against the inspected, accessible sources; independent expert mathematical and publication-priority review have not occurred.

## References

1. H. R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490, first posted 2021-01-16; Sections 2, 4. https://arxiv.org/abs/2101.06490
2. *A regular shattering complex for binary words with no monochromatic triple*, published result dated 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-a-regular-shattering-complex-for-binary-words-with-no-monochroma--a86c7bc37664/RESULT.md
3. *A three-phase sharp Walsh stability law for binary words avoiding \(001\)*, published result dated 2026-11-16, https://github.com/published-finding corpus/2026/blob/main/2026/11/16/SCOPE-a-three-phase-sharp-walsh-stability-law-for-binary-words-avoidin--8fc07c00f15e/RESULT.md
