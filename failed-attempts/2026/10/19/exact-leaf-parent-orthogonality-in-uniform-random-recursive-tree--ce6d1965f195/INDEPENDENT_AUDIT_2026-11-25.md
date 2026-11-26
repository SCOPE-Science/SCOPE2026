# Independent mathematical audit

## correctness

PASS

Rooted leaves, nonleaf vertices with no leaf child, and distinct parents with at least one leaf child do partition the tree. The root differentiation of the labeled EGF deletes the smallest label, leaving an unordered set of increasing subtrees. Thus e^F counts the default root, u−1 adjusts the singleton, and (v−1)(e^(F−uz)−1) adjusts a nonempty set with no singleton. Differentiating formally gives (2); in particular for B=(1−z)b one has B=1−e^(−z)−z+z²/2. The proposed identity gives (1−z)c=z(B′+b)/2−z³/12. Its derivative using B′=e^(−z)−1+z and a=z(2−z)/(2(1−z)) is ab+e^(−z)(a−z), and the constant is zero. Hence (4) is exact. Since (n−1)! trees are divided by n!, moments multiply the extracted coefficient by n; [z^n]a=1/2 for n≥2 and the correction in (4) contributes −n/12 for n≥3. For the leaf variance the conditional leaf increment is 1 minus Bernoulli(L_n/n), giving V_(n+1)=(1−2/n)V_n+1/4 from V_2=0. Thus V_n=n/12, and subtracting from the partition gives Cov(L_n,Q_n)=0. At n=1,2 leaves are deterministic. At n=4 a star has (L,Q)=(3,1), whereas parents (1,1,2) give (2,2), so orthogonality does not generally imply independence. The supplied script was inspected, not run. A fresh exact parent-choice enumerator at /workspace/branches/1393abd7-8492-4aaf-a0c3-e3e688cf0460/record5_fresh_enumeration.py, with record5_enumeration.log in the same directory, checked the partition and all three moments over all 46,233 trees of sizes 2–9; this is corroboration only.

## originality

FAIL

No inspected source was found to print exactly this global leaf-parent covariance. However, it is mechanically implied by the indexed exact joint law at the root and Holmgren–Janson's exact finite-size fringe covariance formula, including its endpoint cases. Specialization to singleton fringe counts gives a sum that telescopes using the alternating factorial increments. The conclusion rests on the explicit derivation below, not on the similarity of the root and global observables, or on an asymptotic limit.

## value

FAIL

The exact orthogonality of two natural dependent counts would be a useful finite-size invariant if not already implied; the short increasing-tree proof is also mathematically sound. But the precise frozen identity follows from the known root transform and the exact fringe covariance lemma by substitution and an elementary factorial telescoping. Neither the equivalent covariance, the known leaf variance, nor the four-vertex witness adds a distinct unknown result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
