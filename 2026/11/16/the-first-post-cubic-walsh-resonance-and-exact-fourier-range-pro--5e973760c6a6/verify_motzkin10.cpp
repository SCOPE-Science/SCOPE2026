// Exact Boolean Fourier computation for length-ten Motzkin excursions.
// C++17; uses only the standard library and integer arithmetic.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
constexpr int steps = 10;
constexpr int coordinates = 2 * steps;
constexpr int group_size = 1 << coordinates;
using i64 = std::int64_t;

void require(bool yes, const std::string& reason) {
    if (!yes) throw std::runtime_error(reason);
}

void enumerate(int pos, int h, int mask, std::vector<int>& paths) {
    if (pos == steps) {
        if (h == 0) paths.push_back(mask);
        return;
    }
    // Horizontal, up, and down steps respectively. The two Boolean
    // coordinates at each position indicate up or down; neither means flat.
    enumerate(pos + 1, h, mask, paths);
    if (h + 1 <= steps - pos - 1)
        enumerate(pos + 1, h + 1, mask | (1 << (2 * pos)), paths);
    if (h > 0)
        enumerate(pos + 1, h - 1, mask | (1 << (2 * pos + 1)), paths);
}

void hadamard(std::vector<i64>& a) {
    for (int width = 1; width < group_size; width *= 2)
        for (int start = 0; start < group_size; start += 2 * width)
            for (int j = 0; j < width; ++j) {
                const i64 u = a[start + j];
                const i64 v = a[start + j + width];
                a[start + j] = u + v;
                a[start + j + width] = u - v;
            }
}

// Independent dynamic-programming evaluation of a character sum. This does
// not inspect the support vector or the results of the Hadamard transform.
i64 direct_transfer(int frequency) {
    std::array<i64, steps + 1> dp{};
    dp[0] = 1;
    for (int pos = 0; pos < steps; ++pos) {
        std::array<i64, steps + 1> next{};
        const i64 up = (frequency & (1 << (2 * pos))) ? -1 : 1;
        const i64 down = (frequency & (1 << (2 * pos + 1))) ? -1 : 1;
        for (int h = 0; h <= pos; ++h) {
            next[h] += dp[h];
            if (h < steps) next[h + 1] += up * dp[h];
            if (h > 0) next[h - 1] += down * dp[h];
        }
        dp = next;
    }
    return dp[0];
}

std::string value_histogram(const std::map<i64, i64>& hist,
                            const std::string& first_label) {
    std::ostringstream out;
    out << first_label << ",count\n";
    for (auto [value, count] : hist) out << value << ',' << count << '\n';
    return out.str();
}

std::string zero_weight_histogram(const std::array<i64, coordinates + 1>& counts) {
    std::ostringstream out;
    out << "weight,zeros\n";
    for (int i = 0; i <= coordinates; ++i) out << i << ',' << counts[i] << '\n';
    return out.str();
}

void write_file(const std::string& file, const std::string& bytes) {
    std::ofstream out(file, std::ios::binary);
    require(static_cast<bool>(out), "cannot write " + file);
    out << bytes;
    require(static_cast<bool>(out), "write failure " + file);
}

void compare_file(const std::string& file, const std::string& bytes) {
    std::ifstream in(file, std::ios::binary);
    require(static_cast<bool>(in), "missing certificate " + file);
    const std::string got((std::istreambuf_iterator<char>(in)),
                           std::istreambuf_iterator<char>());
    require(got == bytes, "certificate mismatch " + file);
}
} // namespace

int main(int argc, char** argv) {
    try {
        const bool emit = argc == 2 && std::string(argv[1]) == "--emit";
        const bool verify = argc == 2 && std::string(argv[1]) == "--verify";
        require(emit || verify, "use --emit or --verify");
        std::vector<int> paths;
        enumerate(0, 0, 0, paths);
        std::sort(paths.begin(), paths.end());
        require(paths.size() == 2188, "unexpected Motzkin cardinality");
        require(std::adjacent_find(paths.begin(), paths.end()) == paths.end(),
                "noninjective step encoding");

        std::vector<i64> multipliers(group_size);
        for (int mask : paths) multipliers[mask] = 1;
        hadamard(multipliers);
        std::map<i64, i64> spectrum_hist;
        std::array<i64, coordinates + 1> zeros_by_weight{};
        i64 zero_count = 0, parseval = 0;
        int first_witness = -1, min_weight = coordinates + 1;
        i64 min_nonzero = 1000000;
        std::vector<i64> projection(group_size);
        for (int frequency = 0; frequency < group_size; ++frequency) {
            const i64 v = multipliers[frequency];
            // Completely independent transfer-matrix calculation for every
            // one of the 1,048,576 signed character sums.
            require(v == direct_transfer(frequency), "independent transfer discrepancy");
            ++spectrum_hist[v];
            parseval += v * v;
            if (v == 0) {
                ++zero_count;
                const int weight = __builtin_popcount(static_cast<unsigned>(frequency));
                ++zeros_by_weight[weight];
                if (weight < min_weight) {
                    min_weight = weight;
                    first_witness = frequency;
                }
            } else {
                projection[frequency] = 1;
                min_nonzero = std::min<i64>(min_nonzero, std::llabs(v));
            }
        }
        require(parseval == static_cast<i64>(group_size) * 2188, "Parseval failure");
        require(zero_count == 67312, "zero count mismatch");
        require(min_weight == 4 && first_witness == 17924, "witness mismatch");
        require(min_nonzero == 2, "nonzero gap mismatch");
        require(spectrum_hist.size() == 302, "number of signed spectral levels");
        require(zeros_by_weight[4] == 48, "minimal-order zero count");
        for (int j = 0; j < 4; ++j) require(zeros_by_weight[j] == 0, "unexpected low-order zero");

        hadamard(projection);
        i64 kernel_abs_sum = 0, kernel_square_sum = 0;
        std::map<i64, i64> kernel_hist;
        for (const i64 v : projection) {
            kernel_abs_sum += std::llabs(v);
            kernel_square_sum += v * v;
            ++kernel_hist[v];
        }
        require(kernel_abs_sum == 52163296, "projection norm numerator mismatch");
        require(kernel_square_sum == static_cast<i64>(group_size) * (group_size - zero_count),
                "projection-kernel Parseval failure");
        require(kernel_hist.size() == 542, "projection kernel level count");

        const std::string spectrum_csv = value_histogram(spectrum_hist, "multiplier");
        const std::string kernel_csv = value_histogram(kernel_hist, "kernel");
        const std::string zero_csv = zero_weight_histogram(zeros_by_weight);
        if (emit) {
            write_file("spectrum.csv", spectrum_csv);
            write_file("projection_kernel.csv", kernel_csv);
            write_file("zeros_by_weight.csv", zero_csv);
        } else {
            compare_file("spectrum.csv", spectrum_csv);
            compare_file("projection_kernel.csv", kernel_csv);
            compare_file("zeros_by_weight.csv", zero_csv);
        }
        std::cout << "MOTZKIN10_WALSH_PASS paths=2188 frequencies=1048576 zeros="
                  << zero_count << " rank=" << group_size - zero_count
                  << " min_zero_weight=" << min_weight
                  << " projection_abs_sum=" << kernel_abs_sum << '\n';
        return 0;
    } catch (const std::exception& ex) {
        std::cerr << "FAIL: " << ex.what() << '\n';
        return 1;
    }
}
