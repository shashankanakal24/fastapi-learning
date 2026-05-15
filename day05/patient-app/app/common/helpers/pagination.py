def paginate(query, page=1, limit=10):

    total = query.count()

    items = query.offset(
        (page - 1) * limit
    ).limit(limit).all()

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "items": items
    }