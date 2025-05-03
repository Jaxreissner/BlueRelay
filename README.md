# BlueRelay

**BlueRelay** is an offline-first emergency alert system that uses Bluetooth chaining to deliver critical alerts to nearby devices—even when there's no internet.

## how it works

1. alerts are created and managed from a central web server (this site)
2. any connected device pulls the latest alerts and starts broadcasting them via Bluetooth
3. nearby offline devices receive the alert and rebroadcast it further
4. when a device gets back online, it reports how far the alert spread
5. the dashboard shows live stats, keywords, and spread info

## key features

- bluetooth-based offline alert sharing
- location-aware alert delivery (coming soon)
- real-time dashboard with device spread counts
- priority tagging: `Critical`, `Warning`, `Alert`

## tech stack

- frontend: Next.js (deployed on Vercel)
- backend: API routes / future database
- alerts: weather.gov API integration (US only)
- Bluetooth handling: native app (coming soon)

## future plans

- build a native mobile app with offline support
- add user location filtering for alerts
- support international alert sources
- develop a public API for custom alert sources

## project status

this is an early-stage project built by a student for real-world emergency use cases. contributions and feedback are welcome!

---

wanna help? open an issue or send a pull request!

BlueRelay © 2025 by Jax Reissner is licensed under CC BY-NC 4.0 
