# Sharp survivor-deletion spectrum of run-two words

## Finding

For an alphabet \(\Sigma\) of size \(q\ge2\), let \(\mathcal R_{q,n}\) consist of the indexed, **linear** words \(w\in\Sigma^n\) with no factor \(aaa\) (for any symbol \(a\)). For \(n\ge1\), define the *survivor-deletion sphere*
\[
\mathcal D(w)=\{w_1\cdots w_{i-1}w_{i+1}\cdots w_n:1\le i\le n\}\cap\mathcal R_{q,n-1},\qquad d(w)=|\mathcal D(w)|.
\]
The empty word is admitted as the length-zero output. The intersection is essential: **both** the source and the retained one-deletion output must respect the run-length-two constraint. This is distinct from an ordinary deletion channel, in which the output need not respect the source constraint.

**Exact local law.** Write the unique maximal-run decomposition as \(w=c_1^{\ell_1}\cdots c_r^{\ell_r}\), with \(1\le\ell_i\le2\) and \(c_i\ne c_{i+1}\). Then
\[
\boxed{d(w)=r-\sum_{i=2}^{r-1}\mathbf1\{\ell_i=1,\ c_{i-1}=c_{i+1},\ \max(\ell_{i-1},\ell_{i+1})=2\}.}\tag{1}
\]

**Exact complete enumerator.** Define \(N_{q,n,j}=|\{w\in\mathcal R_{q,n}:d(w)=j\}|\), and order the four states \(S=\{(1,1),(1,2),(2,1),(2,2)\}\). Let the row vector \(v\) have entries \(v_{(a,b)}=z^{a+b}\), let \(\mathbf1\) be the all-one column vector, and define the four-by-four matrix \(M=M_q(z,u)\) by its only potentially nonzero entries:
\[
M_{(a,b),(b,c)}=z^c\begin{cases}
1+(q-2)u,&b=1\text{ and }(a=2\text{ or }c=2),\\
(q-1)u,&\text{otherwise},
\end{cases}\qquad a,b,c\in\{1,2\}.
\]
Then the entire degree spectrum, for every alphabet size and length, is given by the rational generating function
\[
\boxed{\sum_{n\ge1}\sum_{j\ge0}N_{q,n,j}z^nu^j
=q(z+z^2)u+q(q-1)u^2v(I-M)^{-1}\mathbf1.}\tag{2}
\]
This is an identity of formal power series in \(z\) whose coefficients are polynomials in \(u\); the inverse exists because \(M\) has zero constant term in \(z\).

**Sharp extremes and rigid equality.** For every \(q\ge2\), \(n\ge1\),
\[
\boxed{\min_{w\in\mathcal R_{q,n}}d(w)=\left\lceil\frac{n+2}{4}\right\rceil,\qquad
\max_{w\in\mathcal R_{q,n}}d(w)=n.}\tag{3}
\]
Exactly \(q(q-1)^{n-1}\) words have degree \(n\): those with every adjacent pair unequal. At every length \(n=4h-2\) with \(h\ge1\), exactly \(q(q-1)^{h-1}\) words attain the minimum \(h\). Their maximal run lengths are necessarily
\[
(2,\underbrace{1,1,2,\ldots,1,1,2}_{h-1\text{ groups of }(1,1,2)}),
\]
and, when \(h\ge2\), the two neighbors of each singleton run have identical symbols. At \(h=1\), these are simply the \(q\) constant words of length two. For \(h\ge2\), choose the first run letter arbitrarily; in each successive two-singleton gap, choose its first singleton letter different from the preceding double-run letter, while its second singleton and the next double-run letters are forced. These \(q(q-1)^{h-1}\) choices are all distinct.

## Assumptions and scope

A run is a maximal consecutive block of one symbol. Every word is indexed, not identified with its rotations or reversals. A legal operation deletes exactly one input position, then retains the result *only if it has no run of length three or greater*. Two deletion positions producing the same output are counted once. There is no cyclic wrap-around; \(q=2\) is included. Empty output is counted for \(n=1\). Results (1)–(3) include all finite lengths and require no primality or algebraic structure on the alphabet.

## Proof

**1. Distinct deletion outputs correspond to maximal runs.** If deleting positions \(i<j\) produces the same word, comparison of the two resulting strings between these indices forces \(w_i=w_{i+1}=\cdots=w_j\). Conversely, deleting anywhere within a constant run yields the same word. Thus there is exactly one distinct *unfiltered* one-deletion output per run. Deleting from a run of length two merely shortens that run to one and cannot create a triple. Deleting a singleton first or last run cannot create a triple. Deleting an interior singleton joins the two neighboring runs if their letters agree; its output violates the constraint precisely when they agree and their lengths sum to at least three, or equivalently at least one neighboring length equals two. This proves (1) for every \(r\ge1\), with empty sum when \(r\le2\).

**2. Four-state enumeration.** A word with one maximal run has \(q\) choices of its letter, length one or two, and exactly one deletion output. This contributes \(q(z+z^2)u\). For two or more runs, choosing the first two distinct run letters contributes \(q(q-1)\); their lengths \(a,b\in\{1,2\}\) contribute \(z^{a+b}\); and the two endpoint runs both contribute one surviving deletion output, hence \(u^2\). On appending a run of length \(c\), the previous middle run, of length \(b\), becomes interior. The new letter is different from the current last run letter. Exactly one choice repeats the letter of the run before it; the other \(q-2\) choices do not. If \(b=1\) and either adjacent run has length two, repeating that earlier letter makes its deletion invalid (factor \(1\)), whereas every nonrepeating choice is valid (factor \(u\)). In all other situations all \(q-1\) choices give a valid deletion from the middle run (factor \(u\)). These are exactly the two entries in the definition of \(M\). The newly appended run contributes \(z^c\). Summing all paths of zero or more such extensions from the four initial states yields \(v\sum_{k\ge0}M^k\mathbf1\), proving (2). The end run's deletion remains valid independently of the prior choices; its contribution was included in the initial \(u^2\).

**3. Sharp lower bound.** Let \(k\) be the number of length-two runs, \(s\) the number of singleton runs, \(b\) the number of singleton runs whose deletion survives, and \(t=s-b\). By Step 1, \(d(w)=k+b\) and \(n=2k+s\). Every one of the \(t\) invalid singleton runs is interior and adjacent to at least one length-two run. For a word with at least two runs, let \(e\in\{0,1,2\}\) be the number of end runs having length two. There are at most \(2k-e\) incidences between length-two runs and their neighboring runs; hence \(t\le2k-e\). Each singleton end run certainly survives deletion, so \(b\ge2-e\). Consequently
\[
n=2k+b+t\le4k+b-e=4d(w)-(3b+e)\le4d(w)-2.
\]
The final inequality follows because \(3b+e\ge3(2-e)+e=6-2e\ge2\). If there is only one run, then \(n\le2\), \(d(w)=1\), so the same bound holds. Therefore \(d(w)\ge\lceil(n+2)/4\rceil\).

For sharpness, for each \(h\ge2\) take alternating symbols on successive maximal runs with run lengths \(2,(1,1,2)^{h-1}\). This yields length \(4h-2\), exactly \(h\) surviving deletions (those from its double runs), and no valid singleton deletion. For length \(4h-3\), replace its **final** pair of singleton runs by one singleton run and choose alternating symbols afresh; every singleton still has equal flanking letters and is adjacent to a double run, so again exactly \(h\) deletions survive. For lengths \(4h-4\) and \(4h-5\), instead remove respectively the last two or three symbols of the original length-\((4h-2)\) word. This removes the last double run, creates exactly one legal endpoint singleton and leaves \(h-1\) double runs; again the degree is \(h\). At lengths one and two, a constant word gives degree one. This attains the lower bound for every \(n\ge1\).

**4. Rigidity at maximal span.** Suppose \(n=4h-2\) and \(d(w)=h\), with \(h\ge2\). All inequalities in Step 3 must be equalities. In particular \(3b+e=2\), forcing \(b=0\) and \(e=2\); therefore both end runs are double and every singleton deletion is invalid. Equality \(t=2k-2\) means every potential double-to-neighbor incidence hits a different invalid singleton. There can be no neighboring double runs, no singleton adjacent to two doubles, and no singleton unadjacent to a double. Thus between each consecutive pair of double runs there are **exactly two singleton runs**. Each of those singletons must be flanked by equal-symbol runs, forcing the stated letter relations. The initial double has \(q\) possible symbols. Each of the \(h-1\) gaps introduces one freely selected symbol distinct from the preceding double's symbol; the other singleton and succeeding double symbol are then forced. This gives \(q(q-1)^{h-1}\) words. For \(h=1\), \(n=2\), the minimizers are the \(q\) constant words, consistent with the formula.

**5. Maximum degree.** Every run gives at most one deletion output, so \(d(w)\le r\le n\). Equality requires \(n\) singleton runs, that is, distinct adjacent letters. In such a word deleting any letter yields at worst a new run of length two, so every deletion survives. There are \(q(q-1)^{n-1}\) such words. This establishes (3) and the upper-extreme count.

## Verification

The accompanying standard-library script `checker.py` computes the degree from **three independent descriptions**: direct deletion of each indexed position with deduplication and filtering, a maximal-run local formula, and an independent four-state finite-transfer recurrence. Their full length-by-degree histograms agree exhaustively for \(q=2\) and lengths 1–16, \(q=3\) and lengths 1–10, and \(q=4\) and lengths 1–8, representing 115,544 admissible source words. All claimed minimum, maximum, top-extremizer counts, and sharp-span minimum-extremizer counts within those ranges were checked. Explicit constructions for the four residue classes were tested for \(h=1,\ldots,17\). Run with `python checker.py`; no external modules are required. All-length assertions are proved above; finite checks alone would not establish them.

For example, in the binary case the first six degree polynomials (lengths one through six) are
\[
\begin{aligned}
H_1(u)&=2u,\\
H_2(u)&=2u+2u^2,\\
H_3(u)&=4u^2+2u^3,\\
H_4(u)&=6u^2+2u^3+2u^4,\\
H_5(u)&=2u^2+12u^3+2u^5,\\
H_6(u)&=2u^2+12u^3+10u^4+2u^6.
\end{aligned}
\]
These coefficients can also be generated from (2) without enumerating words.

## Relationship to prior work

Kulkarni and Kiyavash (2012), Section V, study single-deletion code bounds for the *different* \((d,k)\)-run-length-limited source, imposing restrictions on zero runs between singleton ones; they derive constrained-code upper bounds and describe the unfiltered deletion-image language. Their bounds neither impose the present common maximum run length of two on both symbols and on both sides of an edit, nor imply (1)–(3). Liu, Xing, and Zhang (2023) motivate DNA coding under a homopolymer run-length constraint and single-error correction; their code constructions with \(\ell\ge3\) do not count retained deletion spheres in the \(\ell=2\) case.

The conventional \(q\)-ary one-deletion sphere has cardinality equal to the number of maximal runs, a known fact also used in general deletion-ball work. In contrast, imposing the same run limit on the **received** word eliminates precisely the locally classified singleton deletions; the exact full distribution and sharp minimum/census are not consequences of the unrestricted formula alone. Existing distinct-output deletion-pattern collision results count arbitrary outputs, not filtered survivors. There is no claim of a new unconstrained deletion theorem, or of optimal deletion-correcting code size.

## Limitations

The restriction is symmetric max-run-two and linear, with a single deletion; the result does not address cyclic wrap-around, cap three or higher, multiple deletions, or error-correction capacity. The survivor-deletion channel is a constrained *read filter*, not a claim that physical deletions themselves preserve run length. Novelty is assessed against searched literature and related published findings; an equivalent previously unindexed formulation cannot be excluded. Independent mathematical audit has not been performed.

## References

1. S. Liu, C. Xing, Y. Zhang, *Codes with Biochemical Constraints and Single Error Correction for DNA-Based Data Storage*, arXiv:2307.00221, first public version 2023-07-01. https://arxiv.org/abs/2307.00221
2. A. A. Kulkarni, N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128, first public version 2012-11-13. https://arxiv.org/abs/1211.3128
3. Y. Liron, M. Langberg, *A Characterization of the Number of Subsequences Obtained via the Deletion Channel*, arXiv:1202.1644, first public version 2012-02-08. https://arxiv.org/abs/1202.1644
4. *Exact run-pattern collision thresholds and short-deletion extremal counts*, published open research record, 2026-11-02. https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-run-pattern-collision-thresholds-and-short-deletion-extrem--2036e6f8e3be
