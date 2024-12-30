[out:json][timeout:25];
// Gather results within the current bounding box
(
  // Markers (points)
  node["pipeline"="marker"]({{bbox}});
  node["power"="marker"]({{bbox}});
  node["marker"]({{bbox}});

  // Pipelines (lines)
  way["man_made"="pipeline"]({{bbox}});
  relation["man_made"="pipeline"]({{bbox}});

  way["construction:man_made"="pipeline"]({{bbox}});
  relation["construction:man_made"="pipeline"]({{bbox}});

  // Petroleum sites (polygons)
  way["industrial"~"oil|fracking|oil_storage|petroleum_terminal|hydrocarbons|oil_sands|gas|gas_storage|natural_gas|wellsite|well_cluster|refinery"]({{bbox}});
  relation["industrial"~"oil|fracking|oil_storage|petroleum_terminal|hydrocarbons|oil_sands|gas|gas_storage|natural_gas|wellsite|well_cluster|refinery"]({{bbox}});

  way["pipeline"="substation"]({{bbox}});
  relation["pipeline"="substation"]({{bbox}});

  // Pipeline features (points)
  node["pipeline"="valve"]({{bbox}});
  node["pipeline"="flare"]({{bbox}});

  // Petroleum wells (points)
  node["man_made"~"petroleum_well|oil_well"]({{bbox}});

  // Offshore platforms (points and polygons)
  node["man_made"="offshore_platform"]({{bbox}});
  way["man_made"="offshore_platform"]({{bbox}});
  relation["man_made"="offshore_platform"]({{bbox}});
);

// Output the data
out body;
>;
out skel qt;
