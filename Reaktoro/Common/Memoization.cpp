// Reaktoro is a unified framework for modeling chemically reactive systems.
//
// Copyright © 2014-2022 Allan Leal
//
// This library is free software; you can redistribute it and/or
// modify it under the terms of the GNU Lesser General Public
// License as published by the Free Software Foundation; either
// version 2.1 of the License, or (at your option) any later version.
//
// This library is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
// Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with this library. If not, see <http://www.gnu.org/licenses/>.

#include "Memoization.hpp"

namespace Reaktoro {

auto getMemoizationStatus() -> bool&
{
    /// The global variable that holds status if memoization is currently enabled or disabled.
    static bool memoization_active = true;
    return memoization_active;
}

auto Memoization::isEnabled() -> bool
{
    return getMemoizationStatus();
}

auto Memoization::isDisabled() -> bool
{
    return !getMemoizationStatus();
}

auto Memoization::enable() -> void
{
    getMemoizationStatus() = true;
}

auto Memoization::disable() -> void
{
    getMemoizationStatus() = false;
}

} // namespace Reaktoro
