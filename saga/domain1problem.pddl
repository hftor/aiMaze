(define (problem domain1problem)
    (:domain domain1)
    (:requirements :strips :typing :equality)
    (:objects
        WAITRESS - Character
        MAN - Character
        WOMAN - Character
        GUNNI - Character
        DAVID - Character
        GIRL - Character
        BOY - Character
        HOTDOG - Article
        CANDLE - Article
        BREAD - Article
        DOOR - Device
        HAMMER - Device
        RESTAURANT - Location
        FOUNTAIN - Location
        STORE - Location
        HOTDOG_STAND - Location
        DUMPSTER - Location
    )
    (:init
        (IS_AT MAN FOUNTAIN)
        (IS_AT WAITRESS RESTAURANT)
        (IS_AT GUNNI RESTAURANT)
        (IS_AT DAVID RESTAURANT)
        (IS_AT DOOR RESTAURANT)
        (IS_AT HAMMER STORE)
        (IS_AT HOTDOG HOTDOG_STAND)
        (IS_AT GIRL RESTAURANT)
        (IS_AT BOY FOUNTAIN)
        (HAS GIRL CANDLE)
        (HAS WAITRESS BREAD)

        (LOVE MAN WAITRESS)
        (IS_TOOL HAMMER)
        (BROKEN DOOR)
        (MARKETPLACE STORE)
        (FOOD_VENDOR HOTDOG_STAND)
        (EDIBLE HOTDOG)
        (EDIBLE BREAD)
        (LIGHTABLE CANDLE)
        (HAS_FREE_STUFF DUMPSTER)
        (HAS_WATER FOUNTAIN)

        (HUNGRY GUNNI)
        (HUNGRY DAVID)
        (HAPPY GUNNI)
        (HAPPY DAVID)
        (CLUMSY GUNNI)
        (CLUMSY GIRL)
        (POOR DAVID)
        (RICH GUNNI)
    )
    (:goal (and
        ;(not (HUNGRY DAVID))

        ;(HERO BOY)

        ;(SAD GUNNI)
        ;(SAD DAVID)

        ;(MARRIED MAN WAITRESS)
        ;(MARRIED WAITRESS MAN)
    )
  )
)
