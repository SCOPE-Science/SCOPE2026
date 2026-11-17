# Independent mathematical audit

## correctness

PASS

Modulo q forces a unique signed digit at each position: S positions perform ceil(u/q) and T positions perform floor(u/q), proving injectivity. For positive n repeated quotients reach 1 or 0 and terminate exactly if T is infinite; for negative n they reach -1 or 0 and terminate if S is infinite. A length-R support-gap condition forces termination by h+R for q^h<=|n|<q^(h+1), giving H(n)<=1+q^(R+1)|n|. A run of r positions of one sign followed by the opposite support constructs an exact n=+/-q^j witness with height ratio q^r+q^-j, proving necessity. Mechanical floor-increment supports have counts floor(alpha N), balanced gaps, and growth x^alpha/x^(1-alpha). Independent exact integer residue algorithm checked 241 integers in each of 12 q/support patterns for bases 2,3,5, and exact K arithmetic was not substituted for the symbolic proof.

## originality

PASS

Qualified best-of-knowledge PASS for the complete signed-integer coverage iff both supports infinite and sharp bounded-gap iff linear witness-height criterion. The 2026 Ding–Kiss–Niu–Pach–Sándor paper already supplies complementary binary positional injection and polynomial-density context: that at-most-one part is NOT new. Its abstract and accessible citation identify no coverage/height theorem, but its original full text was not obtained; Oxford VPN disconnected. Historical signed-digit representation literature could contain equivalent gap bounds, retained as risk. No claim that search absence proves novelty.

## value

PASS

The difference between injection and coverage is fundamental for subtractive representation functions, and witness magnitude measures quantitative efficiency of unique representations. The theorem characterizes both features exactly for arbitrary complementary positional supports and constructs sharp long-gap counterexamples. This naturally motivated structural criterion is useful independently of any downstream general additive theorem; growth-controlled examples cover every complementary exponent pair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
