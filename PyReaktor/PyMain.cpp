// Reaktor is a C++ library for computational reaction modelling.
//
// Copyright (C) 2014 Allan Leal
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program. If not, see <http://www.gnu.org/licenses/>.

// Boost includes
#include <boost/python.hpp>
namespace py = boost::python;

// PyReaktor includes
#include <PyReaktor/PyCommon.hpp>
#include <PyReaktor/PyCore.hpp>
#include <PyReaktor/PyEquilibrium.hpp>
#include <PyReaktor/PyInterfaces.hpp>
#include <PyReaktor/PyOptimization.hpp>

BOOST_PYTHON_MODULE(reaktor)
{
    // Set numpy as the numeric::array engine
	py::numeric::array::set_module_and_type("numpy", "ndarray");

	// The following export order matters (e.g., Optimization module needs to be exported before Equilibrium module)
    Reaktor::export_Common();
    Reaktor::export_Core();
    Reaktor::export_Optimization();
    Reaktor::export_Equilibrium();
    Reaktor::export_Interfaces();
}
