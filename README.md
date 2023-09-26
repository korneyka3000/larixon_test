Для уменьшения запросов в бд использовал `select_related/prefetch_related` соответственно

Суперюзер создаётся автоматически с кредами `admin`/`admin`

Также сразу подтягиватеся дамп для бд

---

- Запустить docker-compose file:
    ```bash
    docker compose up --build
    ```