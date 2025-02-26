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

// -----------------------------------------------------------------------------
// 👏 Acknowledgements 👏
// -----------------------------------------------------------------------------
// This example was originally authored by:
//   • Svetlana Kyas (14 July 2021)
//
// and since revised by:
//   • Allan Leal (16 July 2021)
//   • Allan Leal (12 October 2022)
// -----------------------------------------------------------------------------

#include <Reaktoro/Reaktoro.hpp>
using namespace Reaktoro;

int main()
{
    // Initialize a thermodynamic database
    SupcrtDatabase db("supcrtbl");

    // Create an aqueous phase automatically selecting all species with given elements, excluding species with tag `organic`
    AqueousPhase aqueousphase(speciate("H O C Ca Mg K Cl Na S N"), exclude("organic"));
    aqueousphase.setActivityModel(chain(
        ActivityModelHKF(),
        ActivityModelDrummond("CO2")
    ));

    // Create a gaseous phase with specified gases
    GaseousPhase gaseousphase("CO2(g) H2O(g)");
    gaseousphase.setActivityModel(ActivityModelPengRobinson());

    // Create a mineral phase
    MineralPhase mineralphase("Calcite");

    // Collect all above-defined phases
    Phases phases(db);
    phases.add(aqueousphase);
    phases.add(gaseousphase);
    phases.add(mineralphase);

    // Construct the chemical system
    ChemicalSystem system(phases);

    // Define initial equilibrium state
    ChemicalState state(system);
    state.temperature(25.0, "celsius");
    state.pressure(1.0, "bar");

    // Specify rainwater composition
    state.set("H2O(aq)", 1.00, "kg");
    state.set("Na+"    , 2.05, "mg");
    state.set("K+"     , 0.35, "mg");
    state.set("Ca+2"   , 1.42, "mg");
    state.set("Mg+2"   , 0.39, "mg");
    state.set("Cl-"    , 3.47, "mg");
    state.set("S2O4-2" , 2.19, "mg");
    state.set("NO3-"   , 0.27, "mg");
    state.set("NH4+"   , 0.41, "mg");

    // Specify the initial amount of calcite
    state.set("Calcite", 10.0, "mol");

    // Create an equilibrium solver and equilibrate given initial state
    EquilibriumSolver solver(system);
    EquilibriumResult result = solver.solve(state);

    // Compute aqueous properties at the calculated equilibrium state
    AqueousProps aprops(state);

    // Output the solubility of calcite in rainwater and other properties of the solution after equilibration
    std::cout << "Solubility of calcite in rainwater: " << (10.0 - state.speciesAmount("Calcite"))/state.speciesMass("H2O(aq)") << " molal" << std::endl;
    std::cout << "pH after equilibration:             " << aprops.pH() << std::endl;
    std::cout << "Ionic strength after equilibration: " << aprops.ionicStrength() << std::endl;

    std::cout << "Equilibrium calculation result: " << std::endl;
    std::cout << " - iterations = " << result.iterations() << std::endl;
    std::cout << " - succeeded  = " << result.succeeded() << std::endl;

    return 0;
}
