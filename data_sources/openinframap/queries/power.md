[out:json][timeout:25];
// Gather results within the current bounding box
(
  // Power lines (lines)
  way["power"~"line|minor_line|cable|minor_cable"]({{bbox}});
  way["construction:power"~"line|minor_line|cable|minor_cable"]({{bbox}});
  way["disused:power"~"line|minor_line|cable|minor_cable"]({{bbox}});
  
  // Power circuit relations
  relation["route"="power"]({{bbox}});
  relation["power"="circuit"]({{bbox}});
  relation["construction:power"="circuit"]({{bbox}});

  // Power towers (points and lines)
  node["power"~"tower|pole|portal"]({{bbox}});
  way["power"~"tower|pole|portal"]({{bbox}});
  node["construction:power"~"tower|pole|portal"]({{bbox}});
  way["construction:power"~"tower|pole|portal"]({{bbox}});
  node["disused:power"~"tower|pole|portal"]({{bbox}});
  way["disused:power"~"tower|pole|portal"]({{bbox}});

  // Power substations (points and polygons)
  node["power"="substation"]({{bbox}});
  way["power"="substation"]({{bbox}});
  relation["power"="substation"]({{bbox}});
  node["construction:power"="substation"]({{bbox}});
  way["construction:power"="substation"]({{bbox}});
  relation["construction:power"="substation"]({{bbox}});

  // Power switchgear (points and polygons)
  node["power"~"switch|transformer|compensator|insulator|terminal|converter"]({{bbox}});
  way["power"~"switch|transformer|compensator|insulator|terminal|converter"]({{bbox}});

  // Power plants (polygons)
  way["power"="plant"]({{bbox}});
  relation["power"="plant"]({{bbox}});
  way["construction:power"="plant"]({{bbox}});
  relation["construction:power"="plant"]({{bbox}});

  // Power generators (points and polygons)
  node["power"="generator"]({{bbox}});
  way["power"="generator"]({{bbox}});
  relation["power"="generator"]({{bbox}});
  node["construction:power"="generator"]({{bbox}});
  way["construction:power"="generator"]({{bbox}});
  relation["construction:power"="generator"]({{bbox}});
  // Utility poles (points)
  node["man_made"="utility_pole"]({{bbox}});

  // Street cabinets (points and polygons)
  node["man_made"="street_cabinet"]({{bbox}});
  way["man_made"="street_cabinet"]({{bbox}});
  relation["man_made"="street_cabinet"]({{bbox}});

);

// Output the data
out body;
>;
out skel qt;
