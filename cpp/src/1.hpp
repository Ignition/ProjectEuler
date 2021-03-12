constexpr auto sum_range(auto low, auto high)
{
    return ((high + low) * (++high - low)) / 2;
}

constexpr auto sum_xs_in_range(auto x, auto low, auto high)
{
    return x*sum_range(1, (++high-low)/x);
}


int problem_1()
{
    auto sum__3s = sum_xs_in_range(3,1,999);
    auto sum__5s = sum_xs_in_range(5,1,999);
    auto sum_15s = sum_xs_in_range(15,1,999);
    return sum__3s + sum__5s - sum_15s;
}
