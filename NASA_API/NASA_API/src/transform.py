def calculate_risk(neo_data):
    """Calculate risk score for asteroids."""
    hazardous_asteroids = []

    for date, asteroids in neo_data.get("near_earth_objects", {}).items():
        for asteroid in asteroids:
            if asteroid["is_potentially_hazardous_asteroid"]:
                size = asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
                speed = float(asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"])
                distance = float(asteroid["close_approach_data"][0]["miss_distance"]["kilometers"])

                risk_score = size * speed / distance
                hazardous_asteroids.append({
                    "name": asteroid["name"],
                    "risk_score": risk_score,
                    "size_km": size,
                    "speed_kmh": speed,
                    "distance_km": distance
                })

    hazardous_asteroids.sort(key=lambda x: x["risk_score"], reverse=True)
    return hazardous_asteroids
