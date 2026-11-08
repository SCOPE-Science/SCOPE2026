// Exhaustive finite certificate for all sizes of Kneser KG(n,2), n >= 5.
// Six edges (the three initial and the three target edges) have twelve
// endpoint slots. Every equality pattern on those slots has a unique
// restricted-growth code, giving Bell(12) = 4,213,597 possibilities.
// All shortest possible sequences can use just edges in the two configurations.
#include <algorithm>
#include <array>
#include <iostream>
#include <utility>

using Edge = std::pair<int, int>;
using Edges = std::array<Edge, 6>;
std::array<int, 12> labels{};
long long patterns = 0, valid_pairs = 0, reached = 0, failures = 0;
int maximal_distance = 0;

bool is_path(const Edges& edges, int state) {
    int degree[12] = {};
    int supported = 0, leaves = 0, middle = 0;
    for (int i = 0; i < 6; ++i) {
        if (state & (1 << i)) {
            ++degree[edges[i].first];
            ++degree[edges[i].second];
        }
    }
    for (int d : degree) {
        supported += (d > 0);
        leaves += (d == 1);
        middle += (d == 2);
    }
    return supported == 4 && leaves == 2 && middle == 2;
}

void test_pattern() {
    ++patterns;
    Edges original{};
    for (int i = 0; i < 6; ++i) {
        int a = labels[2 * i], b = labels[2 * i + 1];
        if (a == b) return;  // No loops.
        if (a > b) std::swap(a, b);
        original[i] = {a, b};
    }
    for (int i = 0; i < 3; ++i)
        for (int j = i + 1; j < 3; ++j)
            if (original[i] == original[j]) return;
    for (int i = 3; i < 6; ++i)
        for (int j = i + 1; j < 6; ++j)
            if (original[i] == original[j]) return;

    Edges unique_edges{};
    int identifiers[6]{};
    int count = 0;
    for (int i = 0; i < 6; ++i) {
        int j = 0;
        while (j < count && unique_edges[j] != original[i]) ++j;
        if (j == count) unique_edges[count++] = original[i];
        identifiers[i] = j;
    }
    int from = 0, target = 0;
    for (int i = 0; i < 3; ++i) from |= 1 << identifiers[i];
    for (int i = 3; i < 6; ++i) target |= 1 << identifiers[i];
    if (is_path(unique_edges, from) || is_path(unique_edges, target)) return;
    ++valid_pairs;

    // Search only three-edge subsets of the union of the two endpoint triples.
    int distance[64];
    std::fill(distance, distance + 64, -1);
    int queue[64]{};
    int head = 0, tail = 0;
    queue[tail++] = from;
    distance[from] = 0;
    while (head < tail) {
        int current = queue[head++];
        if (current == target) break;
        for (int deleted = 0; deleted < count; ++deleted) {
            if (!(current & (1 << deleted))) continue;
            for (int inserted = 0; inserted < count; ++inserted) {
                if (current & (1 << inserted)) continue;
                int next = current ^ (1 << deleted) ^ (1 << inserted);
                if (distance[next] >= 0 || is_path(unique_edges, next)) continue;
                distance[next] = distance[current] + 1;
                queue[tail++] = next;
            }
        }
    }
    if (distance[target] < 0 || distance[target] > 3) {
        ++failures;
        if (failures < 3) {
            std::cerr << "A counterexample was found at canonical pattern "
                      << patterns << ".\n";
        }
    } else {
        ++reached;
        maximal_distance = std::max(maximal_distance, distance[target]);
    }
}

void enumerate_partitions(int position, int current_maximum) {
    if (position == 12) {
        test_pattern();
        return;
    }
    for (int value = 0; value <= current_maximum + 1; ++value) {
        labels[position] = value;
        enumerate_partitions(position + 1, std::max(current_maximum, value));
    }
}

int main() {
    labels[0] = 0;
    enumerate_partitions(1, 0);
    std::cout << "restricted_growth_patterns=" << patterns << '\n'
              << "valid_pairs=" << valid_pairs << '\n'
              << "pairs_connected_in_at_most_3=" << reached << '\n'
              << "counterexamples=" << failures << '\n'
              << "maximum_distance=" << maximal_distance << '\n';
    if (patterns != 4213597 || valid_pairs != 500759 || failures ||
        reached != valid_pairs || maximal_distance != 3) return 1;
    std::cout << "PASS: every valid pair has a path of at most three exchanges\n";
    return 0;
}
