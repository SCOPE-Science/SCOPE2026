# Independent mathematical audit

## correctness

PASS

I reconstructed all 4^10 transitions and checked the census by a separate integer, vectorized lag-equality enumeration. For each starting configuration the first t with an equality F^(t+l)(x)=F^t(x) for l in {1,4,5} exists by t=8. Such equality is possible only on-cycle, and if it holds at any later time it holds on all phases of that cycle, so the earliest such t is the true entry time. Testing the smaller positive lags gives the least period. Canonicalizing the repeated phases gives 1, 530, 6 primitive orbits and all 25 nonzero histogram cells agree with the frozen table and both transcripts. The exact period-basin totals are 436846, 579750, 31980. In the prism any cycle crossing rails uses a positive even number of spokes; a five-cycle with two spokes would require two nonempty rail paths on the same pair of indices with total length three, which is impossible, and four spokes require at least four intervening rail edges. Thus the rail pentagons force shared dihedral action and optional swap. Applying all twenty maps to canonical cycles gives eleven and twenty-one classes of size 10 and 20 at period four; at period five the class of size 2 has basin size 1280 per orbit and the class of size 4 has 7355 per orbit. All 20 depth-eight states are one spatial orbit through 28081, with destination in the latter class (representative 27756 for the witness). The periods divide 20, so the depth bound proves F^28=F^8; F^27 differs from F^7 precisely on the depth-eight states.

## originality

PASS

The exact same record in the catalog is not earlier independent coverage. The strongest same-graph comparison shares two quantitative results but changes the local dynamics; the strongest same-rule comparison changes the graph and its numbers differ. The inspected general results do not give the claimed joint census or unequal per-orbit basins. This passes the distinct four-state prism classification on the available evidence, not priority over the excitation rule or those neighboring censuses.

## value

PASS

The pentagonal prism is a natural small cubic graph with two odd rails, allowing controlled comparison with its three-color predecessor and its four-color Petersen relative. In particular orbit period and readily matching recurrence counts do not capture attractiveness: geometry divides equal-period five-waves into per-orbit basins differing by over a factor of five. The sharp, spatially resolved longest transient and complete depth-by-period counts are concrete benchmarks for finite excitation dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
