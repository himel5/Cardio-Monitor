flowchart LR
  subgraph CLIENTS
    A[Web / Mobile App]
  end

  A -->|HTTPS REST / Webhook| API[API Gateway\nFastAPI or Flask]
  API --> Auth[Auth Module\n(Email+OTP, Google later)]
  API --> Upload[Upload Service\nPDF/Image -> OCR]
  API --> Wearable[Wearable Connector\nUltrahuman, Google Fit later]
  API --> Analysis[Health Analysis Engine\n(rule-based v1)]
  API --> PG[(PostgreSQL\nsummaries & users)]
  API --> MG[(MongoDB Atlas\nraw_reports, wearables)]
  Upload --> OCR[(OCR & Parser\npdfplumber / Tesseract / custom)]
  OCR --> MG
  Wearable --> MG
  MG --> Analysis
  Analysis --> PG
  Analysis -->|results| API
  API --> Storage[File Storage\nRailway Volume / GridFS]
  subgraph CRON
    CronJob[Railway/Render Cron or GitHub Actions]
  end
  CronJob --> Wearable
  CronJob --> Analysis
  CronJob --> API
