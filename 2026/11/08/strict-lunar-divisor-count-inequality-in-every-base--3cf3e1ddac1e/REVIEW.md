# Scientific review

**Correctness — PASS.** The leading digit of a lunar product is the positive minimum of its factors' leading digits, giving the exact digit-length formula. A lunar sum dominates each divisor digitwise, hence numerically, establishing the weak bound. For every multi-digit input, an integer obtained by setting the units digit to zero or one lies below the lunar sum but cannot be a divisor: any factor of it producing the original input would have to be one digit long and preserve the changed units digit. Exact one-digit divisor enumeration handles all remaining cases, including equality at one. The independent finite checker enumerates 1019 inputs across nine bases; proof holds for all bases and positive integers.

**Originality — PASS with priority risk.** The unrestricted conclusion directly establishes the strict base-ten inequality published as Conjecture 5 of Applegate--LeBrun--Sloane (2011), and strengthens it to all integer bases. The paper's Theorem 20 treats divisor sums but does not make the divisor-count comparison. Gross's later maximal-number-of-divisors results address the original paper's distinct Conjectures 2--4, not Conjecture 5. Search comparisons of formulations, number-theoretic record titles, OEIS and original full texts identified no known theorem covering this statement. An unlocated equivalent or later proof remains possible; database silence is not a priority certificate.

**Mathematical value — PASS.** The assertion settles an explicitly published question about a natural pair of arithmetic functions and gives a uniform structural explanation across all bases, including the precise equality boundary. The proof identifies a canonical integer omitted from the divisor set, not simply an isolated example or finite enumeration. Its elementary nature does not diminish the substantive completion of this mathematical question.

Independent mathematical priority and correctness verification have not been performed.

Self-review: passed. Independent audit: not yet performed.
