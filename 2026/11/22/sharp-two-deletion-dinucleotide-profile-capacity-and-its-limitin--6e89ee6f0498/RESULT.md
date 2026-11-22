# Sharp two-deletion dinucleotide-profile capacity and its limiting boundary law

## Finding
Let \(P(w)=(c_{00}(w),c_{01}(w),c_{10}(w),c_{11}(w))\) be the four-coordinate vector of **overlapping adjacent-pair counts** of a finite linear binary word \(w\). For \(n\ge2\), define
\[
 B_2(w)=\left|\left\{P(w\setminus\{i,j\}):0\le i<j<n\right\}\right|,
\]
where deletion removes two distinct indexed positions simultaneously, retains all undeleted letters in their original order, and equal received *profiles*, not merely equal words, count once. The following sharp all-length capacity law holds:
\[
 \boxed{\max_{w\in\{0,1\}^n} B_2(w)=
 \begin{cases}
  1,&n=2,3,\\
  4,6,7,9,11,14,15,16,16,&n=4,5,6,7,8,9,10,11,12\text{ respectively},\\
  17,&n\ge13.
 \end{cases}}
\]
In particular, the universal bound is **seventeen**, and length thirteen is the **first possible saturation length**. Every length \(n\ge13\) has an explicit extremizer:
\[
 w_t=\mathtt{01}\,\mathtt{0}^{t+3}\,\mathtt{10101110},\qquad t=n-13\ge0.
\]
Moreover, for a uniformly random binary word \(W_n\) the random variable \(B_2(W_n)\) converges in distribution to the following six-atom law:

| Number of received profiles | Limiting probability |
|---:|---:|
| 9 | \(1/16\) |
| 10 | \(1/8\) |
| 11 | \(1/16\) |
| 13 | \(3/8\) |
| 14 | \(1/4\) |
| 17 | \(1/8\) |

Convergence of the probabilities is exponentially fast. In particular, the limiting probability of attaining the sharp capacity is exactly \(1/8\).

## Assumptions and scope
Words are indexed, **linear**, and binary, without cyclic wraparound. Both deletions are compulsory, can be adjacent, and may include either endpoint. The output length is \(n-2\); for output lengths zero or one its adjacent-pair profile is the zero quadruple. The capacity law is for every integer \(n\ge2\) and includes arbitrarily long inputs. The limiting distribution assumes independent uniform source bits. No distinction between equal output profiles is made even if the underlying descendant words differ.

## Proof
**1. Local change vectors.** For a pair \(a,b\in\{0,1\}\), let \(e_{ab}\) denote its unit coordinate vector. For an internal single deletion with three-symbol context \(abc\), put
\[
 d(abc)=e_{ac}-e_{ab}-e_{bc}.
\]
All eight triples yield exactly the following four vectors:
\[
 T=\{-e_{00},-e_{11}, e_{00}-e_{01}-e_{10}, e_{11}-e_{01}-e_{10}\}.
\]
Deleting the first symbol changes the profile by \(L=-e_{w_0w_1}\), and deleting the last by \(R=-e_{w_{n-2}w_{n-1}}\). When deleted indices are nonadjacent, the two local changes **add exactly**, including when the intervening segment is one symbol; this follows by comparing the removed and reconnected edges. Thus all nonadjacent two-deletion changes lie in
\[
 (T+T)\cup(L+T)\cup(R+T)\cup\{L+R\},
\]
where \(X+Y\) means pairwise vector sums.

For two *adjacent* deleted symbols with a full four-symbol neighborhood \(abcd\), the change is
\[
 h(abcd)=e_{ad}-e_{ab}-e_{bc}-e_{cd}.
\]
The sixteen four-symbol contexts give exactly six distinct vectors
\[
 A=\{-2e_{00},-2e_{11},-e_{00}-e_{01}-e_{10}+e_{11},
 -e_{00}-e_{11},-e_{01}-e_{10},e_{00}-e_{01}-e_{10}-e_{11}\}.
\]
At the **left** boundary, adjacent deletion of positions \(0,1\) contributes \(-e_{w_0w_1}-e_{w_1w_2}\). At the **right** boundary, adjacent deletion of positions \(n-2,n-1\) contributes \(-e_{w_{n-3}w_{n-2}}-e_{w_{n-2}w_{n-1}}\). These formulas cover every pair of positions when \(n\ge4\) (and the small cases are treated separately).

**2. A fixed boundary envelope.** Write \(\ell=w_0w_1\) and \(r=w_{n-2}w_{n-1}\). Form the finite set \(E_{\ell,r}\) by taking the displayed nonadjacent sums, all six vectors in \(A\), and both possible vectors for each of the two adjacent-boundary deletions, allowing the unspecified third boundary symbol to take either binary value. The actual set of profile changes is a subset of \(E_{\ell,r}\). A direct enumeration of four-element \(T\), six-element \(A\), and the four boundary choices gives this complete **exact integer table of upper-envelope cardinalities**:

| First pair \(\ell\) / last pair \(r\) | 00 | 01 | 10 | 11 |
|:--|---:|---:|---:|---:|
| 00 | 11 | 13 | 14 | 11 |
| 01 | 14 | 14 | **17** | 13 |
| 10 | 13 | **17** | 14 | 14 |
| 11 | 11 | 14 | 13 | 11 |

Every entry is obtainable from at most sixteen short-context evaluations and set union; `verify_local.py` reconstructs the four vectors in \(T\), the six vectors in \(A\), and all sixteen envelope values directly from the stated definitions. Since each entry is at most seventeen, \(B_2(w)\le17\) holds for all \(n\ge4\). At \(n=2,3\) every two-deletion output profile is zero, so the same upper bound holds.

**3. Infinite family of equality witnesses.** Take \(w_0=\mathtt{0100010101110}\). The following complete catalog gives seventeen different changes \(P(\text{deleted word})-P(w_0)\). The pair of deleted positions is zero-indexed. Each displayed pair continues to realize the same change in \(w_t\), after positions at or above four are shifted by \(t\); the local patterns on which the change depends are unchanged by inserting any number of zeroes into the central zero run.

| Change in coordinate order \((00,01,10,11)\) | Deleted positions in \(w_0\) |
|:--|:--|
| \((-2,0,0,0)\) | \((2,3)\) |
| \((-1,-1,-1,1)\) | \((2,6)\) |
| \((-1,-1,0,0)\) | \((0,2)\) |
| \((-1,0,-1,0)\) | \((2,12)\) |
| \((-1,0,0,-1)\) | \((2,9)\) |
| \((0,-2,-2,2)\) | \((6,8)\) |
| \((0,-2,-1,1)\) | \((0,6)\) |
| \((0,-1,-2,1)\) | \((6,12)\) |
| \((0,-1,-1,0)\) | \((0,1)\) |
| \((0,-1,0,-1)\) | \((0,9)\) |
| \((0,0,-1,-1)\) | \((9,12)\) |
| \((0,0,0,-2)\) | \((9,10)\) |
| \((1,-2,-2,1)\) | \((1,6)\) |
| \((1,-2,-1,0)\) | \((0,5)\) |
| \((1,-1,-2,0)\) | \((1,12)\) |
| \((1,-1,-1,-1)\) | \((1,9)\) |
| \((2,-2,-2,0)\) | \((1,5)\) |

The list contains seventeen pairwise different integer quadruples. The upper bound from Step 2 therefore gives equality for every \(t\ge0\), not only for experimentally checked parameter values. To establish that length thirteen is **first**, the separate exhaustive `direct_histogram.cpp` enumerates every one of the \(2^n\) binary words at each of the finite lengths \(2\le n\le12\), computes literal two-deletion descendants and their four-entry profiles, and returns the exact maxima in the Finding. This is a complete finite proof for the finitely many exceptional lengths, not an extrapolation from a sample.

**4. Limiting six-point law.** Fix the first three and last three input bits, denoted \(u,v\in\{0,1\}^3\). All vectors of the following form eventually occur with probability tending to one exponentially fast, **conditional** on these boundary bits:
\[
 F_{u,v}=(T+T)\cup A\cup(L+T)\cup(R+T)\cup\{L+R\}
 \cup\{-e_{u_0u_1}-e_{u_1u_2},
          -e_{v_0v_1}-e_{v_1v_2}\},
\]
where \(L=-e_{u_0u_1}\) and \(R=-e_{v_1v_2}\). Indeed, with exponentially high probability, each of the sixteen binary four-symbol patterns occurs many times in pairwise disjoint interior blocks. This supplies every internal adjacent type and two widely separated instances of every internal three-symbol type, hence all the displayed internal sums and their boundary combinations. Conversely, Step 1 shows no other change is possible. Each of the \(64\) boundary triples \((u,v)\) has exact probability \(1/64\) for \(n\ge6\). Direct finite evaluation of these sets yields the multiplicity table
\[
 \bigl(|\{(u,v):|F_{u,v}|=j\}|\bigr)_{j=9,10,11,13,14,17}
 =(4,8,4,24,16,8).
\]
The extra calculation in `verify_local.py` enumerates these exact sixty-four cases. Dividing by sixty-four gives the stated limiting probabilities. For any fixed pattern, the failure to appear in \(k\) mutually disjoint random length-four blocks has probability \((15/16)^k\); applying the union bound over the finitely many required patterns proves exponential convergence.

## Verification
From the actual source files in this package, run `python3 verify_local.py` and `c++ -O2 -std=c++17 direct_histogram.cpp -o direct_histogram && ./direct_histogram`. Recorded stdout is provided in `verify_local.out` and `direct_histogram.out`, respectively. The Python program implements the local-vector envelope, the seventeen explicit sharpness representatives, and the sixty-four boundary cases. The C++ program uses **literal deletion and histogram counting**, independently of local formulas, over all words of lengths two through thirteen. Its source loops cover every binary word and every ordered pair of distinct deletion positions. Both executables were run successfully.

The theoretical bound and the all-length extremizer follow from the displayed finite local identities and context-preserving construction, not from growing-length enumeration. The first-attainment statement uses a genuinely exhaustive finite check, while the distribution limit uses occurrence probabilities for disjoint length-four blocks. No external proof assistant, independent expert assessment, or large-n empirical assumption is invoked.

## Relationship to prior work
Kiah, Puleo and Milenkovic introduced overlapping-substring profile vectors and their use in DNA storage channels; their analysis centers on global profile classes and coding for synthesis/sequencing errors. A previously published result on one-deletion binary dinucleotide profiles gives six possible observed profiles and their complete one-deletion distribution. A related published result on binary single-insertion profiles gives a separate six-profile law. Neither result concerns the *two-deletion* local profile set considered here, and neither bound implies seventeen or the six-atom limit. A published two-deletion descendant-variance result instead counts distinct **words**, not their collapsed dinucleotide profiles. En Gad's September 2026 preprint develops linear hashing of substring counts for deletion codes and is an especially relevant motivation for studying local count-vector changes; its available abstract describes asymptotic code-size bounds, not this exact finite channel capacity. Its complete text could not be inspected, leaving a priority risk. No claim of independent historical priority is made.

## Limitations
The theorem is confined to the **binary**, **linear**, **two symbol-deletion**, **overlapping adjacent-pair profile** model. It is not a result on full deletion-descendant balls, longer substring counts, nonbinary alphabets, mixed edit operations, or optimal reconstruction code sizes. The limiting distribution is for iid fair bits only. The exhaustive small-length certificate and exact finite local derivations are supplied, but an independently performed scientific audit and complete historical-priority verification remain outstanding; the preprint motivating the question was available only through its abstract in this examination.

## References
1. E. En Gad, *Polynomially larger deletion codes by linear hashing of substring counts*, first public 2026-09-16, arXiv:2609.19493v1, https://arxiv.org/abs/2609.19493.
2. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, first public 2015-02-02, arXiv:1502.00517v1, https://arxiv.org/abs/1502.00517.
3. *The complete one-deletion dinucleotide-profile ball distribution for binary words*, publicly accessible research result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-the-complete-one-deletion-dinucleotide-profile-ball-distribution--294c530e44d7/RESULT.md.
4. *Exact single-insertion dinucleotide-profile ambiguity in binary words*, publicly accessible research result, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-exact-single-insertion-dinucleotide-profile-ambiguity-in-binary--7545727346c0/RESULT.md.
5. *Exact fluctuations of two-deletion output counts over finite alphabets*, publicly accessible research result, https://github.com/published-finding corpus/2026/blob/main/2026/11/2/SCOPE-exact-fluctuations-of-two-deletion-output-counts-over-finite-alp--b1a2bd3da18e/RESULT.md.
