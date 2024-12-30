[out:json][timeout:25];
// Gather results within the current bounding box
(
  // Telecom cables (lines)
  way["communication"~"line|cable"]({{bbox}});
  relation["communication"~"line|cable"]({{bbox}});

  way["construction:communication"~"line|cable"]({{bbox}});
  relation["construction:communication"~"line|cable"]({{bbox}});

  // Telecom buildings (points and polygons)
  node["building"~"data_center|data_centre|telephone_exchange"]({{bbox}});
  way["building"~"data_center|data_centre|telephone_exchange"]({{bbox}});
  relation["building"~"data_center|data_centre|telephone_exchange"]({{bbox}});

  node["telecom"~"data_center|data_centre|central_office|exchange"]({{bbox}});
  way["telecom"~"data_center|data_centre|central_office|exchange"]({{bbox}});
  relation["telecom"~"data_center|data_centre|central_office|exchange"]({{bbox}});

  node["office"="telecommunication"]({{bbox}});
  way["office"="telecommunication"]({{bbox}});
  relation["office"="telecommunication"]({{bbox}});

  node["man_made"="telephone_office"]({{bbox}});
  way["man_made"="telephone_office"]({{bbox}});
  relation["man_made"="telephone_office"]({{bbox}});

  // Telecom locations (points and polygons)
  node["telecom"~"connection_point|distribution_point"]({{bbox}});
  way["telecom"~"connection_point|distribution_point"]({{bbox}});
  relation["telecom"~"connection_point|distribution_point"]({{bbox}});

  // Masts (points and polygons)
  node["man_made"~"mast|tower|communications_tower"]({{bbox}});
  way["man_made"~"mast|tower|communications_tower"]({{bbox}});
  relation["man_made"~"mast|tower|communications_tower"]({{bbox}});

  node["tower:type"="communication"]({{bbox}});
  way["tower:type"="communication"]({{bbox}});
  relation["tower:type"="communication"]({{bbox}});

  // Telecom antennas (points and polygons)
  node["man_made"="antenna"]({{bbox}});
  way["man_made"="antenna"]({{bbox}});
  relation["man_made"="antenna"]({{bbox}});
);

// Output the data
out body;
>;
out skel qt;
