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
        BARBERSHOP - Location
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
        (CUTS_HAIR BARBERSHOP)
        (IS_HIRING STORE)

        (HUNGRY GUNNI)
        (HUNGRY MAN)
        (HAPPY GUNNI)
        (HAPPY DAVID)
        (CLUMSY GUNNI)
        (CLUMSY GIRL)
        (POOR MAN)
        (RICH GUNNI)
        (RICH DAVID)
        (HAS_GOOD_ADVICE GUNNI)
    )
    (:goal (and
        (HERO BOY)
    )
  )
)
