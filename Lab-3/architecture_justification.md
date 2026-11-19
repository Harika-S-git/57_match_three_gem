# Lab 3 - Architecture Selection and Justification

**Harika S | SRN PES2UG24AM062 | Section 5A**

**Scenario:** Self-Service Coffee Kiosk. Customers choose Espresso, Americano, or Latte in Small or Large sizes, pay by credit card, and receive a printed receipt.

## Architecture Selection
We chose **Layered Architecture**. The presentation layer has the touchscreen. The business/integration layer has the Order Manager, Payment Service and Receipt Printer Adapter. The data layer holds the Menu and Pricing Repository. Printer hardware and the external card gateway are dependencies.

## Two reasons
1. **Separation of concerns:** The touchscreen handles selections, the Order Manager coordinates orders, Payment Service authorizes the credit card, and the repository manages prices. Each part can change without rewriting the rest.
2. **Appropriate complexity:** A single kiosk has a small, sequential workflow and limited independent scaling needs. Layered architecture is easier to maintain than microservices and does not depend on a central remote order server.

## Security Advantage
Confine card authorization to Payment Service via TLS to a payment gateway; avoid storing full card data, validate input at the business layer, and restrict access to the menu repository.

## Performance Benefit
Local or cached menu reads make touchscreen interactions responsive. The gateway call is needed only for card authorization, after which receipt printing can begin.

## Alternatives Considered
Microservices provide independent deployment but unnecessary network and operations complexity. Client-server offers central control but increases server and network dependence.

**Diagram:** 7 components, 6 interfaces. The PlantUML source uses interface balls and required dependency arrows; the diagrams.net source is editable.
