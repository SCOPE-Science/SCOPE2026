# Independent mathematical audit

## correctness

PASS

For g(u)=u²e^(−u) on u≥0 and zero otherwise, g and g′ match continuously across zero. On each active interval e^t H′ is a concave quadratic with negative leading coefficient. Its signs at the second and third arrivals equal the signs of 2−δ and F(δ)=2−δ+4(1−δ)e^(−δ), respectively. F decreases up through 2 and stays negative thereafter. The largest possible negative impulse slope is M=2(1+√2)e^(−2−√2); the degree-four Taylor lower bound for e^(1+√2) exceeds 4(1+√2) by 11/8−2√2/3>0, giving 2M<e^−1 and a positive slope one time unit after either new arrival when δ>1 (using the applicable active impulses). Concavity then yields one down-crossing after the last arrival for δ≤δ₀, an additional down-crossing between arrivals for δ₀<δ≤2, and the isolated first-pulse maximum for δ>2. At δ₀ the third-arrival slope is zero but positive on both adjacent sides; at 2 the same holds at the second arrival. Neither shoulder adds a maximum. This also verifies the one-crest two-pulse comparison for δ≤2. Replay: RESULT.md, Proof, lines 29–62; independent high-precision bisection gives δ₀=1.537805488887338839… . The supplied checker was inspected as text, not executed, and is not needed for the all-real proof. Scope is strict maxima at positive times for three equal, equally spaced point inputs and three identical linear reservoirs.

## originality

PASS

The supported distinct claim is the full three-input Nash-kernel crest classification, especially the resolved two-crest window below the isolated pulse's mode. The closest inspected same-kernel results concern two pulses; the strongest distinct same-date three-pulse match is for the logistic kernel and has no two-crest phase. This is a bounded scientific comparison, not certification of historical priority.

## value

PASS

The exact first transition answers whether collective inputs can resolve two discharge crests before pairwise resolution is possible, not merely whether an isolated numerical example can do so. The complete gap ranges and shoulder endpoints provide a reproducible benchmark for idealized routing. It does not predict observational peak resolution or flood risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
