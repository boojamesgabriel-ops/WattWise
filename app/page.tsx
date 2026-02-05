'use client'

import { Authenticated, Unauthenticated } from 'convex/react'
import { SignInButton, UserButton, useUser } from '@clerk/nextjs'
import { useRouter } from 'next/navigation'
import { useEffect } from 'react'
import SyncUser from '@/components/SyncUser'
import AppliancesPage from './appliances/page'
import BudgetsPage from './budgets/page'
import LandingPage from "@/src/components/LandingPage"

export default function Home() {
  const { isSignedIn } = useUser()
  const router = useRouter()

  // Redirect to dashboard when logged in
  useEffect(() => {
    if (isSignedIn) {
      router.push('/dashboard')
    }
  }, [isSignedIn, router])

  return (
    <>
      <Authenticated>
        {/* User will be redirected, but show briefly */}
        <div className="p-4">
          <UserButton />
        </div>
        <SyncUser />
        <AppliancesPage />
        <BudgetsPage />
      </Authenticated>
      
      <Unauthenticated>
        <LandingPage />
      </Unauthenticated>
    </>
  )
}
