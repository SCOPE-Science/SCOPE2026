# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **failed**.

- Correctness: **PASS**. The centralizer-difference identity is correct: the standard normal-cyclic-Sylow formula rewrites as \(\psi(G)=A\psi(C)+p^\alpha(\psi(H)-\psi(C))\), and \(A=\psi(C_{p^\alpha})\) is coprime to \(p\). For \(H=C_{q^\beta}\) with action image \(q^\gamma\), the kernel is \(C_{q^{\beta-\gamma}}\), the cyclic prime-power sum difference factors by \(q^{2(\beta-\gamma)+1}(q^{2\gamma}-1)/(q+1)\), and the action gives \(q^\gamma\mid p-1\), so the \(q\)-power factor is coprime to \(A\). The resulting exact gcd formula and strict nondivisibility inequality are algebraically valid. Independent compatible parameter checks reproduced the formula.
- Originality: **FAIL**. A published 20 September 2026 result already proves the strictly broader theorem that every semidirect product with a noncentral normal cyclic Sylow subgroup and coprime complement is not psi-divisible. Its proof displays the same decomposition \(\psi(G)=A\psi(C)+p^\alpha(\psi(H)-\psi(C))\). Because \(\gcd(A,p)=1\), taking a gcd with \(A\) immediately gives the audited centralizer-difference identity; specializing \(H\) and \(C\) to cyclic prime-power groups then gives the advertised exact gcd by one standard cyclic-sum subtraction. Thus both the nondivisibility conclusion and the quantitative core are mechanically implied by the earlier published result.
- Scientific value: **FAIL**. After the broader 20 September theorem is treated as prior, the surviving quantitative formula is a direct gcd-and-substitution calculation from an identity already printed in that prior proof. The prime-power complement and image/kernel corollaries therefore do not constitute a separately motivated mathematical gap under the stated value standard.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and
`INDEPENDENT_AUDIT_2026-10-01.json`. Earlier review evidence is preserved in
`AUDIT.json` and is not relabeled as independent evidence.
