'use client'

import React from 'react'
import { useUser } from '@clerk/nextjs'
import { useMutation } from 'convex/react'
import { api } from '../convex/_generated/api'

export default function SyncUser() {
  const { user } = useUser()
  const storeUser = useMutation(api.users.storeUser)

  React.useEffect(() => {
    if (!user) return
    storeUser({
      clerkId: user.id,
      email: user.primaryEmailAddress?.emailAddress ?? '',
    }).catch(() => {})
  }, [user, storeUser])

  return null
}