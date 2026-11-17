# Independent mathematical audit

## correctness

PASS

For W=P^k, greedy embedding advances copies exactly at weak descents, so v occurs iff D(v)≤k-1. Minimal absence forces D(v)=k, endpoint weak descents, and every interior Δ_i=d(v_{i-1},v_i)+d(v_i,v_{i+1})-d(v_{i-1},v_{i+1})=1. Ascents are isolated and induce strict two-step increases in BOTH parity tracks; with a ascents, remaining k-a-1 nonincreasing two-step edges imply k≥a+1+2floor((a-1)/(q-1)). Doubled staircase blocks T_h=00 11 ... (h-1)(h-1), repeated and supplemented with leading zeros, attain each allowed ascent count. Inverting gives exactly lengths k+1 to k+1+(q-1)floor((k-1)/(q+1))+min((k-1) mod(q+1),q-1), q≥4. Independently brute-forced all candidate MAS for q=4,k=1,2,3: length supports {2},{3,4},{4,5,6}, respectively, agreeing. Inspected separate finite-state/literal verifier, not using its output as universal proof.

## originality

PASS

Sharp length-support interval for all permutation powers with q≥4 is not given by the inspected 2021 same-host exponential MAS construction or by the 2025 arbitrary-host algorithm for finding one longest MAS. It goes beyond a single computed value: supplies exact closed formula, no gaps and structural witnesses uniformly in two unbounded parameters. Special smaller alphabets and a quaternary length/count generating-function finding overlap in limited cases, not all q≥4.

## value

PASS

Permutation powers are natural canonical subsequence hosts; the exact contiguous spectrum of minimal absent lengths and sharp longest-length slope 2q/(q+1) solve a meaningful all-parameter combinatorial invariant. The parity-track obstruction and explicit extremal staircase witnesses provide structural interpretation beyond generic instance-by-instance algorithms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
