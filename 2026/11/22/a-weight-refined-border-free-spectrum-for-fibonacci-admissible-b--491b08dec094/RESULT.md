# A weight-refined border-free spectrum for Fibonacci-admissible binary words

## Finding

For a binary word, a *border* is a nonempty proper prefix that equals a suffix of the same length. A word is *unbordered* if it has no border. Let \(\mathcal L_n\) denote the length-\(n\) binary words containing no adjacent `11`, for \(n\ge 1\). Define

\[
U_n(t)=\sum_{\substack{w\in\mathcal L_n\\w\text{ unbordered}}}t^{\lvert w\rvert_1},\qquad U(z,t)=\sum_{n\ge1}U_n(t)z^n.
\]

Then the **complete weight-refined length distribution** is the unique formal solution, with zero constant term, of

\[
\boxed{(1-z-tz^2)U(z,t)+U(z^2,t^2)=(1+t)z+t(1+t)z^2(1-z).}
\tag{1}
\]

In particular, writing \(u_n=U_n(1)\), the counts start, at lengths \(1\) through \(21\),

\[
2,2,2,2,4,4,8,10,18,24,42,62,104,158,262,410,672,1064,1736,2776,4512.
\]

For \(k\ge2\) they satisfy

\[
u_{2k+1}=u_{2k}+u_{2k-1},\qquad
u_{2k}=u_{2k-1}+u_{2k-2}-u_k,
\tag{2}
\]

with \(u_1=u_2=u_3=2\). The proportion of unbordered words among all words avoiding `11` has the **strictly positive, explicit limit**

\[
\boxed{\lim_{n\to\infty}\frac{u_n}{F_{n+2}}
=p=2\varphi^{-3}-\sum_{k=2}^{\infty}u_k\varphi^{-2k-1}
=0.1556298471279007014\ldots,}
\tag{3}
\]

where \(F_0=0\), \(F_1=1\), and \(\varphi=(1+\sqrt5)/2\). The convergence error is \(O(\varphi^{-n/2})\). For a truncation before term \(k=K\), its explicit upper approximation \(p_K\) satisfies

\[
p_K-\varphi^{2-K}\le p\le p_K,\qquad
p_K=2\varphi^{-3}-\sum_{k=2}^{K-1}u_k\varphi^{-2k-1}\quad(K\ge2).
\tag{4}
\]

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). Avoidance of `11` is checked linearly, not cyclically. Borders are **contiguous** equality of proper prefix and suffix, not Abelian borders or subsequences. The empty word is excluded from the generating function. The variable \(t\) counts occurrences of symbol `1`; coefficients in equation (1) are nonnegative integers. Equations (1)–(4) hold over all admissible word lengths, not just the verified finite range. The limiting density concerns uniform sampling from \(\mathcal L_n\), not independent fair bits conditioned on an infinite two-sided shift.

## Proof

**1. Unique shortest-border decomposition.** Every bordered word has a unique shortest nonempty border \(v\). That border must itself be unbordered: otherwise a border of \(v\) is a shorter border of the original word. A shortest border has length at most half the word length, so the original word factors uniquely as \(v m v\). Conversely, if \(v\) is unbordered and both copies are legal with the intervening word \(m\), then the shortest border is \(v\). Indeed, any shorter border would also be a border of \(v\).

**2. Legal middle words.** Write

\[
D(z,t)=1-z-tz^2,\quad T(z,t)=\frac{1+tz}{D(z,t)},\quad M(z,t)=\frac1{D(z,t)}.
\]

Here \(T\) counts all `11`-avoiding words including the empty word, and \(M\) counts legal middles with exactly one forced adjacent zero boundary: its length-zero coefficient is one; at length \(j\ge1\), the remaining \(j-1\) symbols have polynomial \([z^{j-1}]T\). In fact \(M(z,t)=1+zT(z,t)\), which follows directly from \(D+z(1+tz)=1\).

If the shortest border \(v\) has length at least two, its first and last symbols differ (otherwise it has a length-one border). Consequently, each junction with the middle forces precisely one zero endpoint; the middle possibilities are counted by \(M\), irrespective of the orientation of \(v\). Repeating \(v\) doubles its number of ones, giving the weight factor \(t^{2\lvert v\rvert_1}\). The contribution over shortest borders of length at least two is

\[
M(z,t)\bigl(U(z^2,t^2)-(1+t^2)z^2\bigr).
\tag{5}
\]

A shortest border `0` permits any legal middle, giving \(z^2T(z,t)\). A shortest border `1` forces a nonempty middle that starts and ends with zero; its middle series is \(zM(z,t)\), hence contributes \(t^2z^3M(z,t)\). These three classes are disjoint and exhaustive. Subtracting them from all nonempty legal words yields

\[
U=(T-1)-z^2T-t^2z^3M-M\bigl(U(z^2,t^2)-(1+t^2)z^2\bigr).
\]

Multiplying by \(D\) and simplifying gives equation (1), proving its coefficients are exactly the claimed word counts. The coefficient at length \(n\) of \(U(z^2,t^2)\) uses only the already-defined coefficient at \(n/2\), so equation (1) uniquely determines all coefficients by induction.

**3. Scalar recurrence.** Set \(t=1\) in equation (1). At lengths \(1,2,3\) it gives two words each. For \(n\ge4\), equating coefficients yields

\[
u_n=u_{n-1}+u_{n-2}-\mathbf1_{2\mid n}u_{n/2},
\]

which is equivalent to equation (2). Since \(U(z^2,1)\) begins with \(2z^2\), isolating its remaining terms and expanding \(1/(1-z-z^2)=\sum_{j\ge0}F_{j+1}z^j\) also gives, for every \(n\ge2\),

\[
u_n=2F_{n-1}-\sum_{k=2}^{\lfloor n/2\rfloor}u_kF_{n-2k+1}.
\tag{6}
\]

**4. Limiting density with a certified tail.** Exactly \(F_{n+2}\) admissible words have length \(n\), so \(0\le u_n\le F_{n+2}\le\varphi^{n+1}\). In equation (6), divide by \(F_{n+2}\) and use the standard Fibonacci/Binet asymptotic. The absolute bound on the resulting infinite sum follows from

\[
0\le u_k\varphi^{-2k-1}\le\varphi^{-k}.
\]

Its tail from \(k=K\) is at most \(\sum_{k\ge K}\varphi^{-k}=\varphi^{2-K}\), proving equation (4) and justifying the limit in (3) by dominated convergence. The Binet error for the bounded finite portion, plus the tail starting at \(k\asymp n/2\), gives \(O(\varphi^{-n/2})\); the exponentially smaller conjugate-root term is absorbed. Taking \(K=10\) in (4) gives a positive lower bound, while \(K=100\) certifies the displayed decimal prefix.

## Verification

Run both standard-library Python programs from the directory containing them:

```sh
python3 verify_bruteforce.py
python3 verify_decomposition.py
```

The first enumerates all \(F_{n+2}\) allowed words at each length \(1\le n\le21\), independently tests every nonempty proper prefix/suffix pair, and compares full one-count histograms with equation (1). The second counts unique shortest-border sandwiches by polynomial convolution, compares them with a separately implemented coefficient recurrence through length \(150\), and bounds the limiting proportion by equation (4) using 60-digit decimal arithmetic. At \(K=100\), the computed enclosure is

\[
0.15562984712790070140427027\ldots\le p\le
0.15562984712790070140757557\ldots.
\]

These computations test, but do not replace, the general combinatorial proof above.

## Relationship to prior work

The ordinary binary unbordered-word recurrence (without a local forbidden pattern) and the unconstrained fixed-weight enumeration are established subjects in combinatorics on words. Harju and Nowotka study fixed-weight bordered/primitive words; the unrestricted standard recurrence counts all binary unbordered words. Neither enumeration can simply be restricted to the `11`-avoiding language because the legality of the middle in the shortest-border decomposition depends on the boundary letters of the repeated border. The new equation (1) explicitly handles this local constraint and refines by weight; equation (3) quantifies the resulting constrained proportion. These are distinct statements rather than new names for known unconditioned counts.

Related analyses of finite Fibonacci substitution words, Abelian borders, and special fixed-marker spectra have a different domain or equivalence relation. No claim is made that an exhaustive literature search certifies priority. Earlier unindexed constrained enumerations, notably unavailable complete expositions of work on fixed-weight bordered words, remain possible precedents.

## Limitations

The result does not determine maximum sizes of *sets* of mutually cross-bifix-free words, error-correcting code capacities, circular-word statistics, or variants forbidding other factors. The density calculation is specific to linear `11`-avoidance. The numerical enclosure uses proved tail bounds, not an extrapolation from finite counts. The independent mathematical audit has not been performed.

## References

- T. Harju and D. Nowotka, *Counting bordered and primitive words with a fixed weight*, Theoretical Computer Science **340** (2005), 273–279, https://doi.org/10.1016/j.tcs.2005.03.040. Corresponding mathematical sequence dated 2004-11-11 at https://oeis.org/A099766.
- D. Gabric and J. Shallit, *Smallest and Largest Block Palindrome Factorizations*, 2023 preprint, https://arxiv.org/abs/2302.13147 (classical unconstrained border-free recurrence context).
- M. A. Nyblom, *Counting palindromic binary strings without \(r\)-runs of ones*, 2013, https://studylib.net/doc/10375993/counting-palindromic-binary-strings-r-runs-of-ones-without (local-run avoidance under a different global symmetry constraint).
- Standard Fibonacci-language counting: the number of length-\(n\) binary strings avoiding `11` is \(F_{n+2}\); this classical identity is used as a premise, not claimed as new.
