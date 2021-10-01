// Reaktoro is a unified framework for modeling chemically reactive systems.
//
// Copyright © 2014-2021 Allan Leal
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

// pybind11 includes
#include <Reaktoro/pybind11.hxx>

// Reaktoro includes
#include <Reaktoro/Core/ChemicalProps.hpp>
#include <Reaktoro/Core/ChemicalState.hpp>
using namespace Reaktoro;

void exportChemicalProps(py::module& m)
{
    py::class_<ChemicalProps>(m, "ChemicalProps")
        .def(py::init<const ChemicalSystem&>())
        .def(py::init<const ChemicalState&>())
        .def("update", py::overload_cast<const ChemicalState&>(&ChemicalProps::update))
        .def("update", py::overload_cast<const real&, const real&, ArrayXrConstRef>(&ChemicalProps::update))
        .def("update", py::overload_cast<ArrayXrConstRef>(&ChemicalProps::update))
        .def("update", py::overload_cast<ArrayXdConstRef>(&ChemicalProps::update))
        .def("updateIdeal", py::overload_cast<const ChemicalState&>(&ChemicalProps::updateIdeal))
        .def("updateIdeal", py::overload_cast<const real&, const real&, ArrayXrConstRef>(&ChemicalProps::updateIdeal))
        .def("system", &ChemicalProps::system, return_internal_ref)
        .def("phaseProps", py::overload_cast<Index>(&ChemicalProps::phaseProps), return_internal_ref)
        .def("phaseProps", py::overload_cast<Index>(&ChemicalProps::phaseProps, py::const_), return_internal_ref)
        .def("temperature", &ChemicalProps::temperature)
        .def("pressure", &ChemicalProps::pressure)
        .def("charge", &ChemicalProps::charge)
        .def("elementAmount", &ChemicalProps::elementAmount)
        .def("elementAmountInPhase", &ChemicalProps::elementAmountInPhase)
        .def("elementAmountAmongSpecies", &ChemicalProps::elementAmountAmongSpecies)
        .def("elementMass", &ChemicalProps::elementMass)
        .def("elementMassInPhase", &ChemicalProps::elementMassInPhase)
        .def("elementMassAmongSpecies", &ChemicalProps::elementMassAmongSpecies)
        .def("elementAmounts", &ChemicalProps::elementAmounts)
        .def("elementAmountsInPhase", &ChemicalProps::elementAmountsInPhase)
        .def("elementAmountsAmongSpecies", &ChemicalProps::elementAmountsAmongSpecies)
        .def("speciesAmount", &ChemicalProps::speciesAmount)
        .def("speciesMass", &ChemicalProps::speciesMass)
        .def("speciesMoleFraction", &ChemicalProps::speciesMoleFraction)
        .def("speciesConcentration", &ChemicalProps::speciesConcentration)
        .def("speciesConcentrationLg", &ChemicalProps::speciesConcentrationLg)
        .def("speciesConcentrationLn", &ChemicalProps::speciesConcentrationLn)
        .def("speciesActivityCoefficient", &ChemicalProps::speciesActivityCoefficient)
        .def("speciesActivityCoefficientLg", &ChemicalProps::speciesActivityCoefficientLg)
        .def("speciesActivityCoefficientLn", &ChemicalProps::speciesActivityCoefficientLn)
        .def("speciesActivity", &ChemicalProps::speciesActivity)
        .def("speciesActivityLg", &ChemicalProps::speciesActivityLg)
        .def("speciesActivityLn", &ChemicalProps::speciesActivityLn)
        .def("speciesChemicalPotential", &ChemicalProps::speciesChemicalPotential)
        .def("speciesStandardVolume", &ChemicalProps::speciesStandardVolume)
        .def("speciesStandardVolumeT", &ChemicalProps::speciesStandardVolumeT)
        .def("speciesStandardVolumeP", &ChemicalProps::speciesStandardVolumeP)
        .def("speciesStandardGibbsEnergy", &ChemicalProps::speciesStandardGibbsEnergy)
        .def("speciesStandardEnthalpy", &ChemicalProps::speciesStandardEnthalpy)
        .def("speciesStandardEntropy", &ChemicalProps::speciesStandardEntropy)
        .def("speciesStandardInternalEnergy", &ChemicalProps::speciesStandardInternalEnergy)
        .def("speciesStandardHelmholtzEnergy", &ChemicalProps::speciesStandardHelmholtzEnergy)
        .def("speciesStandardHeatCapacityConstP", &ChemicalProps::speciesStandardHeatCapacityConstP)
        .def("speciesStandardHeatCapacityConstV", &ChemicalProps::speciesStandardHeatCapacityConstV)
        .def("speciesAmounts", &ChemicalProps::speciesAmounts, return_internal_ref)
        .def("speciesMasses", &ChemicalProps::speciesMasses)
        .def("speciesMoleFractions", &ChemicalProps::speciesMoleFractions, return_internal_ref)
        .def("speciesConcentrationsLn", &ChemicalProps::speciesConcentrationsLn)
        .def("speciesActivityCoefficientsLn", &ChemicalProps::speciesActivityCoefficientsLn, return_internal_ref)
        .def("speciesActivitiesLn", &ChemicalProps::speciesActivitiesLn, return_internal_ref)
        .def("speciesChemicalPotentials", &ChemicalProps::speciesChemicalPotentials, return_internal_ref)
        .def("speciesStandardVolumes", &ChemicalProps::speciesStandardVolumes, return_internal_ref)
        .def("speciesStandardVolumesT", &ChemicalProps::speciesStandardVolumesT, return_internal_ref)
        .def("speciesStandardVolumesP", &ChemicalProps::speciesStandardVolumesP, return_internal_ref)
        .def("speciesStandardGibbsEnergies", &ChemicalProps::speciesStandardGibbsEnergies, return_internal_ref)
        .def("speciesStandardEnthalpies", &ChemicalProps::speciesStandardEnthalpies, return_internal_ref)
        .def("speciesStandardEntropies", &ChemicalProps::speciesStandardEntropies)
        .def("speciesStandardInternalEnergies", &ChemicalProps::speciesStandardInternalEnergies)
        .def("speciesStandardHelmholtzEnergies", &ChemicalProps::speciesStandardHelmholtzEnergies)
        .def("speciesStandardHeatCapacitiesConstP", &ChemicalProps::speciesStandardHeatCapacitiesConstP, return_internal_ref)
        .def("speciesStandardHeatCapacitiesConstV", &ChemicalProps::speciesStandardHeatCapacitiesConstV, return_internal_ref)
        .def("phaseAmount", &ChemicalProps::phaseAmount)
        .def("phaseMass", &ChemicalProps::phaseMass)
        .def("phaseVolume", &ChemicalProps::phaseVolume)
        .def("amount", &ChemicalProps::amount)
        .def("mass", &ChemicalProps::mass)
        .def("volume", &ChemicalProps::volume)
        .def("volumeT", &ChemicalProps::volumeT)
        .def("volumeP", &ChemicalProps::volumeP)
        .def("gibbsEnergy", &ChemicalProps::gibbsEnergy)
        .def("enthalpy", &ChemicalProps::enthalpy)
        .def("entropy", &ChemicalProps::entropy)
        .def("internalEnergy", &ChemicalProps::internalEnergy)
        .def("helmholtzEnergy", &ChemicalProps::helmholtzEnergy)
        .def("output", py::overload_cast<std::ostream&>(&ChemicalProps::output, py::const_))
        .def("output", py::overload_cast<const String&>(&ChemicalProps::output, py::const_))
        .def("__repr__", [](const ChemicalProps& self) { std::stringstream ss; ss << self; return ss.str(); })
        ;
}
