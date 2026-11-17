# Exact singleton reconstruction counts for cyclic binary trigram profiles

## Finding

Let \(U_n\) be the number of length-\(n\) cyclic binary trigram-count profiles with exactly one realization **modulo cyclic rotation**. For all \(n\ge1\),

\[U(z)=\sum_{n\ge1}U_nz^n=\frac{2z+3z^2+4z^3+4z^4+3z^5+5z^6+6z^7+7z^8+5z^9-z^{11}-4z^{12}-2z^{14}}{(1-z^3)(1-z^4)}.\]

Thus \(U_n=\tfrac83n+O(1)\) as \(n\to\infty\). The initial values for \(n=1,\ldots,18\) are
\(2,3,4,6,8,12,16,19,22,24,28,29,34,34,38,41,44,44\).

## Assumptions and scope

A cyclic word is an indexed vector \(w\in\{0,1\}^n\) with subscripts interpreted modulo \(n\); this convention applies also for \(n=1,2\). Its observation is the eight-entry vector \(c(w)=(c_{abc}(w))_{a,b,c\in\{0,1\}}\), where \(c_{abc}(w)=|\{i\in\mathbb Z/n:(w_i,w_{i+1},w_{i+2})=(a,b,c)\}|\). Two words represent the same source when related by a cyclic rotation (not by reversal or complementation). A profile is a *singleton* when exactly one rotation class yields it. The statistic counts distinct singleton profiles, rather than indexed sources, all realizable profiles, or single linear words.

## Proof

**1. Profiles and runs.** Constant words give two singleton profiles at every length. A nonconstant word decomposes uniquely up to rotation into \(k\ge1\) alternating zero-runs and one-runs with positive lengths \(Z=(z_1,\ldots,z_k)\), \(O=(o_1,\ldots,o_k)\). The rotation classes of cyclic words correspond exactly to simultaneous cyclic shifts of both \(k\)-tuples. Write \(s_0=\sum z_i\), \(s_1=\sum o_i\), and let \(a,b\) count zero- and one-runs of length one, respectively. These five integers \((s_0,s_1,k,a,b)\) determine the full trigram profile, since
\[
\begin{aligned}
c_{101}&=a,&c_{010}&=b,\\
c_{001}=c_{100}&=k-a,&c_{011}=c_{110}&=k-b,\\
c_{000}&=s_0-2k+a,&c_{111}&=s_1-2k+b.
\end{aligned}
\]
Conversely, the profile recovers \(s_0,s_1\) from its middle-symbol marginals, recovers \(a,b\) from \(c_{101},c_{010}\), and recovers \(k=c_{001}+c_{101}\). Thus a fixed profile is precisely a product of two prescribed sets of run-length vectors, modulo diagonal cyclic shift.

**2. The one-color rotation orbit criterion.** Fix \(k\ge2\), a run total \(s\), and \(a\) runs of length one; put \(j=k-a\) and \(e=s-a-2j\). If \(j=0\), there is one vector, all ones, with \(s=k\). If \(j\ge1\) and \(e\ge0\), the number of *ordered* admissible vectors is
\[
N(k,s,a)=\binom kj\binom{e+j-1}{j-1}.
\]
A cyclic-shift orbit has size at most \(k\). An explicit examination of the binomial factors shows that the admissible vectors comprise a **single** rotation orbit exactly in these cases: all \(k\) runs have length one; all have length two; exactly one run has length at least two and the remaining runs length one; if \(k\ge3\), exactly one run has length one and the remaining runs length two; or exactly one run has length three and the remaining runs length two. In the first two cases there is one vector (call it *rigid*); in the other cases there are \(k\) vectors, permuted freely and transitively by cyclic shift (call these *flexible*). To justify exhaustion, if \(2\le j\le k-2\), then \(\binom kj>k\) for \(k\ge4\), except the empty range at \(k\le3\). For \(j=k-1\), \(\binom kj=k\), requiring \(e=0\); for \(j=k\), \(\binom{e+k-1}{k-1}\le k\) precisely for \(e=0\) or \(e=1\). The \(j=1\) case has exactly \(k\) vectors for every \(e\ge0\). At \(k=2\), the \(j=k-1\) case is already included in \(j=1\), so it must not be counted twice.

**3. Paired orbit criterion.** For a fixed five-parameter profile with \(k\ge2\), its zero-run and one-run vector sets are acted on by the same cyclic group \(C_k\). The product has exactly one diagonal orbit if and only if each factor has one orbit and at least one factor is rigid. Indeed, projecting a transitive product action onto either factor preserves transitivity; two flexible factors have \(k^2\) ordered pairs, too many for a \(k\)-element group to act transitively; a rigid factor paired with a flexible or rigid factor is transitive. The same conclusion remains valid at \(k=2\).

**4. Sum over run counts.** For \(k\ge2\), the generating polynomials in *symbol totals* for rigid one-color run choices and flexible ones are, respectively,
\[
R_k(z)=z^k+z^{2k},\qquad F_k(z)=\frac{z^{k+1}}{1-z}+\boldsymbol{1}_{k\ge3}z^{2k-1}+z^{2k+1}.
\]
Here the indicator term avoids double-counting the \(k=2\) case. For \(k=1\), any positive pair of run lengths gives one rotation class, contributing \(z^2/(1-z)^2\). Constant words contribute \(2z/(1-z)\). By the paired orbit criterion, each \(k\ge2\) contributes \(R_k(z)^2+2R_k(z)F_k(z)\). Therefore
\[
U(z)=\frac{2z}{1-z}+\frac{z^2}{(1-z)^2}+\sum_{k\ge2}\bigl(R_k(z)^2+2R_k(z)F_k(z)\bigr).
\]
Summing each geometric series and reducing the common denominator gives the boxed rational function. Its numerator takes value \(32\) at \(z=1\), while \((1-z^3)(1-z^4)\sim12(1-z)^2\), proving the asymptotic \(U_n=\frac83n+O(1)\), with bounded periodic fluctuation from the other roots of unity.

## Verification

Run `python3 verify_direct.py` to enumerate all indexed words through \(n=18\), form each full eight-entry cyclic trigram profile and count profiles whose rotation-class fiber is singleton. Expected terminal line: `DIRECT_OK`. Run `python3 verify_runs.py` for independent finite tests of the one-color and paired rotation criteria and comparison of 120 exact coefficients against the rational recurrence. Expected terminal lines: `RUN_TRANSITIVITY_OK`, `PAIRED_TRANSITIVITY_OK`, and `RATIONAL_SERIES_OK`. The infinite theorem relies on the run-orbit counting proof above, not on finite computation.

## Relationship to prior work

Kiah, Puleo and Milenkovic [1] develop de Bruijn-flow and DNA-profile enumeration for *all* realizable count vectors and decoding from representative Eulerian trails; those results do not imply how many count vectors have a unique cyclic source without a separate multiplicity analysis. Karhumäki et al. [2] study singleton \(k\)-abelian classes of *linear words* with noncyclic factors and endpoints, characterizing their structures and bounding their numbers. Such a singleton is not the same as a cyclic trigram profile with a unique rotation class: in particular, rotating an observed cyclic word changes endpoints but not this profile. The present result is a closed-form cyclic, binary, fixed-window-three singleton *profile count* for all lengths.

## Limitations

The alphabet is binary, the window consists of ordered cyclic trigrams, and source words are identified only by rotation. No formula for larger alphabets, longer windows, noise, or linear-endpoint observations is claimed. Priority relative to potentially unindexed tables or later specializations of general \(k\)-abelian theory has not been independently audited. The attached tests provide reproducibility, not an external certification.

## References

[1] H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Storage Channels* (first version, October 31, 2014), revised as *Codes for DNA Sequence Profiles*, arXiv:1410.8837, https://arxiv.org/abs/1410.8837; full revised text https://arxiv.org/html/1410.8837v2.

[2] J. Karhumäki, S. Puzynina, M. Rao, M. A. Whiteland, *On cardinalities of \(k\)-abelian equivalence classes* (May 11, 2016), arXiv:1605.03319, https://arxiv.org/html/1605.03319v1.
