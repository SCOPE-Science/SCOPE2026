# Scientific review

**Correctness: PASS.** Maximal independent sets of a path correspond bijectively to selected-position sequences with initial position 1 or 2, internal gaps 2 or 3, and terminal position \(n-1\) or \(n\). The resulting signed recurrence has base data \(F_1=s_1,F_2=s_2,F_3=s_1s_3\). Its seven-step matrix product is explicitly \(\begin{psmallmatrix}3&4&2\\-2&-3&-2\\2&2&1\end{psmallmatrix}\), fixing the output row \((1,1,0)\). The four base zeros at lengths 2, 3, 5, 9 propagate to every exceptional length. For all other lengths the unsigned Padovan count is odd, so every Walsh multiplier is odd and cannot vanish. Independent finite enumeration and integer matrix checks pass.

**Originality: PASS subject to bounded historical comparison.** Relevant primary texts on maximal independent set counts, including Bisdorff–Marichal and Nagy, were compared with the *weighted vertexwise Walsh statement*, not merely by subject terms. The unsigned Padovan recurrence is acknowledged as known. An indexed result on independent-support Fourier *interpolation* concerns invertibility of a restricted Fourier submatrix; it does not imply this convolution spectrum. Another indexed record about Padovan residues modulo powers of two concerns recurrence orbit statistics, not Walsh zeros of maximal independent sets. The public indexed summaries did not establish the seven-period convolution criterion. Risk remains of an inaccessible or unindexed equivalent signed specialization.

**Value: PASS.** Invertibility of convolution with a combinatorially constrained support is the exact information-recovery question on the binary vertex cube. This result gives a complete all-length boundary with a nontrivial seven-period resonance and explicit infinite families of disappearing Walsh modes. The construction is a short, reusable transfer-matrix certificate; it is not a mere numerical prefix, arbitrary slice, or reformulation of the known unsigned Padovan counts.

**Limits.** Only invertibility is classified; no general rank formula for singular lengths is claimed. Independent expert validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
