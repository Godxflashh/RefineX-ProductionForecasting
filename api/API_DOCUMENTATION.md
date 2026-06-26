# API Documentation

## Base URL

http://127.0.0.1:5000

---

## GET /

Returns project information.

Example

{
    "project":"RefineX",
    "module":"Production Forecasting",
    "status":"Running"
}

---

## GET /health

Returns API health.

Example

{
    "status":"Healthy"
}

---

## GET /predict

Returns refinery production forecast.

Example

{
    "next_month_prediction":34820.96,
    "next_3_month_average":41796.96,
    "next_12_month_average":39413.49
}