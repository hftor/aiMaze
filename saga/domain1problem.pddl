(define (problem domain1problem)
    (:domain domain1)
    (:requirements :strips :typing :equality)
    (:objects
            PRINCESS - Character
            FROG - Character
            KING - Character
            FROG_SERVANT - Character
            MAN - Character
            WOMAN - Character
            WITCH - Character
            RAPUNZEL - Character
            KING_SON - Character
            GOLD_BALL - Article
            TLC - Article
            RADISH - Article
            PALACE - Location
            GARDEN - Location
            FOUNTAIN - Location
            ROAD - Location
            TOWER - Location
    )
    (:init
        (IS_AT PRINCESS PALACE)
        (IS_AT FROG FOUNTAIN)
        (IS_AT KING PALACE)
        (IS_AT FROG_SERVANT TOWER)
        (IS_AT MAN ROAD)
        (IS_AT WOMAN GARDEN)
        (IS_AT WITCH TOWER)
        (IS_AT RAPUNZEL GARDEN)
        (IS_AT KING_SON ROAD)
        (HAS PRINCESS TLC)
        (HAS PRINCESS GOLD_BALL)
        (HAS WITCH RADISH)
        (EDIBLE RADISH)
        (HUNGRY WOMAN)
      )
    (:goal (and
        (not (HAS WITCH RADISH))
        (not (HAS MAN RADISH))
        (HAS FROG RADISH)
    )
    )
)
