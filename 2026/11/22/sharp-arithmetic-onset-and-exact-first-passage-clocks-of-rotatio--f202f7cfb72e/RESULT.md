# Sharp arithmetic onset and exact first-passage clocks of rotational symmetry in cyclic Boolean erosion

## Finding
For cyclic binary words, the first appearance of each rotational stabilizer under one-sided Boolean erosion is an explicit maximum over mismatched original run lengths. A nonzero, nonuniform symmetric transient can arise from an initially asymmetric word **exactly** on composite rings of length at least ten.

## Assumptions and scope
Let \(n\ge2\). The state space is \(\{0,1\}^{\mathbb Z/n\mathbb Z}\), and \((Ex)_i=x_ix_{i+1}\), with indices interpreted modulo \(n\). A shift \(d\in\mathbb Z/n\mathbb Z\) fixes \(y\) when \(y_{i+d}=y_i\) for all \(i\). We call \(y\) nonuniform when it contains both symbols.

For any state other than the all-one word, define its *run-start profile* \(h_i(x)\) to be the length \(\ell\) of the maximal forward cyclic one-run starting at \(i\) if \(x_i=1\) and \(x_{i-1}=0\), and zero otherwise. The all-zero word has the all-zero profile. Every positive entry is at most \(n-1\). For a nonzero shift \(d\), set
\[
T_d(x)=\max\left(\{0\}\cup\{\max(h_i(x),h_{i+d}(x)):h_i(x)\ne h_{i+d}(x),\ i\in\mathbb Z/n\mathbb Z\}\right).
\]
For the all-one word, put \(T_d=0\).

**Theorem.** For every \(x\), every \(d\ne0\), and every integer \(t\ge0\),
\[
E^t(x)\text{ is fixed by }d\quad\Longleftrightarrow\quad t\ge T_d(x).
\]
Thus its stabilizer at time \(t\) is exactly \(\{0\}\cup\{d\ne0:T_d(x)\le t\}\). Also, an initially asymmetric word can reach a nonuniform shift-symmetric word before extinction if and only if \(n\ge10\) is composite. Such a transition can occur in one update.

## Proof
**Iterated erosion and run starts.** By induction on \(t\), \((E^t x)_i=\prod_{j=0}^t x_{i+j}\). If \(x\) is neither all zero nor all one, every original maximal one-run beginning at \(i\) with length \(\ell\) is replaced after \(t\) updates by a one-run of length \((\ell-t)_+\), at the same starting index if positive; the intervening zero gaps persist. Consequently the run-start profile of \(E^t x\) is precisely \(((h_i(x)-t)_+)_{i\in\mathbb Z/n\mathbb Z}\). The claim also holds for the all-zero word; the all-one word remains fixed.

A nonuniform binary cyclic word is determined uniquely by its run-start profile, and the profile transforms equivariantly under translation. Hence shift \(d\) fixes \(E^t x\) if and only if \((h_i-t)_+=(h_{i+d}-t)_+\) for all \(i\). Two nonnegative integers \(a,b\) have equal positive-part truncations \((a-t)_+=(b-t)_+\) exactly when either \(a=b\) or \(t\ge\max(a,b)\). Taking the maximum over discrepancies proves the claimed clock formula and stabilizer description.

**Necessity of a long proper period.** Suppose \(x\) is initially asymmetric, yet \(y=E^t x\) is nonuniform with a nonzero rotational symmetry at some \(t\ge1\). Let \(d<n\) be the least positive period of \(y\), so \(d\mid n\). The positive entries of the truncated run-start profile occur exactly at original one-runs of length at least \(t+1\). Their starting positions and lengths are periodic modulo \(d\). If *all* original one-runs survive, the original profile is itself \(d\)-periodic, contradicting asymmetry. Therefore there is an original disappeared one-run of length \(e\) with \(1\le e\le t\). It lies between consecutive surviving one-runs, whose start-to-start distance is at most \(d\) because the surviving profile is nonempty and \(d\)-periodic. One surviving run has original length \(\ell\ge t+1\). There must be at least one zero separating it from the vanished run and another zero separating the vanished run from the next surviving run. Thus the distance between those two surviving starts is at least \(\ell+1+e+1\ge t+4\ge5\). Hence \(d\ge5\), so \(n\) is composite and at least ten.

**Sufficiency.** Conversely, let \(n\) have a proper divisor \(d\ge5\). Define \(x_i=1\) precisely at positions with \(i\equiv0,1\pmod d\), together with the single additional position \(i=3\); all other sites are zero. There are \(n/d\ge2\) runs of length two and exactly one run of length one. Every rotational symmetry would have to preserve the unique singleton-run starting position and is therefore trivial. Under one erosion update, the singleton vanishes, and each two-run shrinks to a singleton at index \(i\equiv0\pmod d\). The result is nonuniform and has period \(d\). Finally, a positive integer \(n\) admits a proper divisor \(d\ge5\) precisely when it is composite and at least ten: for composite \(n\ge10\), division by its smallest prime factor gives such a divisor (check \(n=10\) as the smallest case). This proves the complete dichotomy.

## Verification
The supplied standalone Python checker exhausts the shift-wise clock formula for every binary initial state on rings \(2\le n\le12\), every nonzero displacement and every time \(0\le t\le n\); this amounts to 81,924 initial-state/displacement tests with all times included. It separately exhausts every initially asymmetric binary state on rings \(2\le n\le16\), verifying the existence dichotomy and the positive-case counts. The mathematical theorem is proved by the above run decomposition for all ring lengths; finite checks do not substitute for this argument.

## Relationship to prior work
Banda, Caughman, and Lehman (2026) establish that spatial symmetry cannot be lost under a translation-equivariant cellular automaton and investigate symmetry enumeration. The present result derives exact *birth times* of every symmetry for a specific nonlinear Boolean erosion map and a sharp arithmetic criterion for genuinely nonuniform symmetry acquisition. Run-length evaluation of binary erosion is established in mathematical morphology, including Kim, Kim, and Kim (2005); it is used as a basic ingredient, not presented as new.

## Limitations
The clock formula applies to this one-sided nearest-neighbor binary AND map, not to arbitrary cellular automata. Its existence dichotomy specifically excludes symmetry that appears only when the state becomes uniformly zero. The result does not provide a closed formula for the number of asymmetric words exhibiting nonuniform symmetry acquisition at each \(n\); exhaustive counts through length sixteen serve only as finite checks. Equivalent unindexed older classifications cannot be completely excluded.

## References
1. P. Banda, J. Caughman, and T. Lehman, *Shift-Symmetric Configurations in d-Dimensional Cellular Automata: Enumeration, Bounds, Irreversibility, and Detection*, arXiv:2611.15751v1, first public 2026-11-11, https://arxiv.org/pdf/2611.15751.
2. S.-W. Kim, S.-D. Kim, and J.-H. Kim, *Fast algorithms for binary dilation and erosion using run-length encoding*, ETRI Journal (2005), https://doi.org/10.4218/etrij.05.0205.0013.
