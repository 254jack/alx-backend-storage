-- list all bands wtih Glam rock as their main style --
SELECT band_name, 
    CASE
        WHEN split IS NULL THEN "Unknown"
        ELSE 2022 - formed
    END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
