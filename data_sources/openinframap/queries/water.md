[out:json][timeout:25];
// Gather results within the current bounding box
(
  // Water treatment plants
  node["man_made"="water_works"]({{bbox}});
  way["man_made"="water_works"]({{bbox}});
  relation["man_made"="water_works"]({{bbox}});

  node["man_made"="desalination_plant"]({{bbox}});
  way["man_made"="desalination_plant"]({{bbox}});
  relation["man_made"="desalination_plant"]({{bbox}});

  // Wastewater plants
  node["man_made"="wastewater_plant"]({{bbox}});
  way["man_made"="wastewater_plant"]({{bbox}});
  relation["man_made"="wastewater_plant"]({{bbox}});

  // Pumping stations
  node["man_made"="pumping_station"]({{bbox}});
  way["man_made"="pumping_station"]({{bbox}});
  relation["man_made"="pumping_station"]({{bbox}});

  // Water towers
  node["man_made"="water_tower"]({{bbox}});
  way["man_made"="water_tower"]({{bbox}});
  relation["man_made"="water_tower"]({{bbox}});

  // Water wells
  node["man_made"="water_well"]({{bbox}});
  way["man_made"="water_well"]({{bbox}});
  relation["man_made"="water_well"]({{bbox}});

  // Pressurized waterways
  node["waterway"="pressurised"]({{bbox}});
  way["waterway"="pressurised"]({{bbox}});
  relation["waterway"="pressurised"]({{bbox}});

  // Water reservoirs
  node["man_made"="reservoir_covered"]({{bbox}});
  way["man_made"="reservoir_covered"]({{bbox}});
  relation["man_made"="reservoir_covered"]({{bbox}});

  node["water"="reservoir"]({{bbox}});
  way["water"="reservoir"]({{bbox}});
  relation["water"="reservoir"]({{bbox}});
);

// Output the data
out body;
>;
out skel qt;
