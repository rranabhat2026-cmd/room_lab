# Transportation lens

Use this to turn a general advance into a concrete transportation
engineering idea. The goal is an idea Rahul could actually test with
accessible data in weeks, not a slogan.

## Problem map

Match the advance to the problem it could change, not to a buzzword:

| Area | Typical problems | Common data |
|---|---|---|
| Traffic flow and control | state estimation, short-term forecasting, signal timing, ramp metering, shockwaves | loop detectors (PeMS, state DOT feeds), probe speeds, NGSIM / highD-style trajectories |
| Safety | crash frequency and severity, hotspot ranking, near-miss detection, systemic safety | state crash databases, FARS, video, roadway inventories |
| Networks and GIS | network modeling, accessibility, routing, spatial graphs | OpenStreetMap / OSMnx, GTFS, census and LEHD |
| Demand and behavior | trip generation, mode choice, travel time reliability, activity models | household travel surveys (NHTS), app and probe data, counts |
| Transit | ridership, scheduling, reliability, bunching | GTFS and GTFS-realtime, APC and AVL |
| Active transportation | bike and pedestrian demand, level of stress, network gaps | counters, Strava Metro-type aggregates, OSM |
| Freight and logistics | truck routing, parking, port and corridor flows | FAF, truck GPS aggregates |
| Infrastructure and assets | pavement and bridge deterioration, inspection, maintenance planning | inspection records, images, sensor data |
| CAV and connectivity | mixed traffic, platooning, cooperative control, V2X security | simulation (SUMO, CARLA), field pilots |
| Resilience and energy | evacuation, disruption recovery, EV charging placement | network plus hazard and grid data |
| Planning and policy | scenario analysis, equity, project prioritization | MPO models, public reports |

## Integration template (per developed item)

1. **The advance in one line** and what is actually new (S#).
2. **Transportation problem it could change** (from the map) and why the
   current approach falls short there.
3. **Mechanism:** why it should help, in engineering terms. If it is a
   physics-informed method, name the governing relationship (for example
   LWR conservation `∂ρ/∂t + ∂(ρ·v(ρ))/∂x = 0`, car-following models,
   Wardrop equilibrium) and its regime of validity.
4. **Simplest credible test:** data source, study unit, split that matches
   the claim (future period, unseen corridor or city), baseline (a classical
   one is required: ARIMA, Kalman filter, cell transmission model,
   historical average, logit), metric, and an estimate of effort in hours.
5. **What would make it fail:** data scarcity, distribution shift, sensor
   noise, regulation, compute cost, agency adoption barriers.
6. **Who would care:** a researcher, agency, operator, consultant, or
   company, and what they would pay attention to.
7. **Verdict:** `Try now` / `Watch` / `Not for transportation yet`, with one
   sentence.

## Honesty rules

- A method winning on a general benchmark says little about traffic data
  with missing sensors, incidents, and holidays. Say what transfer is
  assumed.
- Real network geometry with synthetic demand must be labeled as such.
- Keep unrelated projects separate (for example an FDOT cybersecurity
  review and a bicycle GIS analysis); link them only when the hypothesis
  benefits.
